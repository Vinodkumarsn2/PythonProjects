from tkinter.filedialog import *
from tkinter import messagebox
import img2pdf
from PDFDragDrop import *
import os

#To Open any file from the PC
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

#iconfile = resource_path('pdfIcon.png')

class img_doc():
    def __init__(self, filename):
        self.filename = filename
        self.displayname = filename.split('/')[-1]

def load():
    fs = askopenfilenames(filetypes=(('Image File', '*.jpg *.jpeg *.jfif *.tif *.tiff *.png *.bmp *.gif'), ('All Files', '*.*')))
    root.update()
    #fs = askopenfilenames()
    for f in fs:
        imgObj = img_doc(f)
        imgObj_list.append(imgObj)
        listbox.insert(END, imgObj.displayname)
        print(imgObj.displayname)

def remove():
    index = int(listbox.curselection()[0])
    imgObj_list.pop(index)
    listbox.delete(ANCHOR)

def convert_pdf():
    output_filename = asksaveasfilename(filetypes=(('PDF File', '*.pdf'), ('All files', '*.*')))

    for img in imgObj_list:
        img_list.append(img.filename)
        print(img_list)

    output_filename = output_filename + '.pdf'
    with open(output_filename,"wb") as f:
        f.write(img2pdf.convert(img_list))
    f.close()
    opendpdf = messagebox.askyesno("PDF Generated", "Do you want to open the Converted PDF?")
    if opendpdf:
        os.startfile(output_filename)
    root.quit()

img_list =[]
imgObj_list = []

root = Tk()
root.title('Images To PDF')

#icon = PhotoImage(file="C:/Data/PythonFileServ/PyCharm/ImageToPDF/pdfIcon.png")
icon = PhotoImage(file='pdfIcon.png')
root.iconphoto(False, icon)
#root.tk.call('wm','iconphoto',root._w, icon)

Label(root,text='Image to PDF',fg='blue').grid(row=0,column=0,columnspan=2)

Button(root,text='Add Images', command=load).grid(row=2, column=0)
Button(root,text='Remove Images', command=remove).grid(row=3, column=0)

listbox = DragDropListbox(root,imgObj_list)
listbox.bind('<<ListboxSelect>>')
listbox.grid(row=1, rowspan=4, column=1)

Button(root, text='Convert to Single PDF ', command=convert_pdf, width=20, fg='brown').grid(row=5, column=0, columnspan=4)

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
