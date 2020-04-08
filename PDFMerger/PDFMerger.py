#Here we can add mutliple files in single Add button
from tkinter.filedialog import *
from tkinter import messagebox
import PyPDF2
from PDFDragDrop import *
#NOTE: WE can move the below CLASS and load_pdf function to another python file and import the things
#NOTE2: I have imported the Drag and Drop functions from the Python file PDFDragDrop.py
class pdf_doc():
    def __init__(self, filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = int(1)
        self.end = int(self.pages)

    def add_to_writer(self, writer):
        for i in range(self.start-1, self.end):
            writer.addPage(self.pdf.getPage(i))

def load_pdf(filename):
    f = open(filename, 'rb')
    return PyPDF2.PdfFileReader(f)


def load():
    fs = askopenfilenames(filetypes=(('PDF File', '*.pdf'), ('All Files', '*.*')))
    for f in fs:
        pdf = pdf_doc(f)
        pdf_list.append(pdf)
        listbox.insert(END, pdf.display)
        print(pdf_list)

def remove():
    index = int(listbox.curselection()[0])
    pdf_list.pop(index)
    listbox.delete(ANCHOR)
    print(pdf_list)

    firstindex = 0
    value = listbox.get(firstindex)
    filename.set(value)
    pages.set(pdf_list[firstindex].pages)
    start.set(pdf_list[firstindex].start)
    end.set(pdf_list[firstindex].end)

def save_pdf():
    #get the writer
    writer = PyPDF2.PdfFileWriter()

    if pdf_list:
        output_filename = asksaveasfilename(filetypes=(('PDF File', '*.pdf'), ('All files', '*.*')))
        output_filename = output_filename+'.pdf'
        print(output_filename)
        output_file = open(output_filename, 'wb')


        for doc in pdf_list:
            doc.add_to_writer(writer)

        writer.write(output_file)
        output_file.close()
        openmergedpdf = messagebox.askyesno("Merge Completed", "Do you want to open the merged PDF?")
        if openmergedpdf:
            os.startfile(output_filename)
        root.quit()

def display(*args):
    index = int(listbox.curselection()[0])
    value = listbox.get(index)
    filename.set(value)
    pages.set(pdf_list[index].pages)
    start.set(pdf_list[index].start)
    end.set(pdf_list[index].end)

def set_start(*args):
    index = int(listbox.curselection()[0])
    if start.get():
        try:
            pdf_list[index].start = int(start.get())
            if ((pdf_list[index].start <= 0) | (pdf_list[index].start > pdf_list[index].end)):
                pdf_list[index].start = 1
        except ValueError:
            messagebox.showerror(title='ValueError',message='Enter Valid Integer')

def set_end(*args):
    index = int(listbox.curselection()[0])
    if end.get():
        try:
            pdf_list[index].end = int(end.get())
            if ((pdf_list[index].end <= 0) | (pdf_list[index].end < pdf_list[index].end) | (pdf_list[index].end > pdf_list[index].pages)):
                pdf_list[index].end =  int(pdf_list[index].pages)
        except ValueError:
            messagebox.showerror(title='ValueError', message='Enter Valid Integer')

#list to hold the PDF objects of type pdf_doc class
pdf_list = []

root = Tk()
root.title('PDF Merger')
icon = PhotoImage(file="pdfIcon.png")
root.iconphoto(False, icon)

filename = StringVar()
pages = StringVar()
start = StringVar()
end = StringVar()

Label(root,text='PDF Merger', foreground='blue').grid(row=0,column=0,columnspan=4)

Button(root,text='Add PDFs', command=load).grid(row=2, column=0)
Button(root,text='Remove PDF', command=remove).grid(row=3, column=0)

#listbox from the DragDrop library. extra parameter is passed here.
listbox = DragDropListbox(root,pdf_list)
listbox.bind('<<ListboxSelect>>', display)
listbox.grid(row=1, rowspan=4, column=1)

Label(root,text='Selected File: ').grid(row=1, column=2)
Label(root, textvariable=filename,width=20).grid(row=1,column=3,sticky=(N,S,E,W))

Label(root, text='Total Pages: ').grid(row=2, column=2)
Label(root, textvariable=pages).grid(row=2, column=3)

Label(root, text='Start Page: ').grid(row=3, column=2)
s= Entry(root, textvariable=start, width=3)
s.grid(row=3, column=3)

Label(root, text='End Page: ').grid(row=4, column=2)
e= Entry(root, textvariable=end, width=3)
e.grid(row=4, column=3)

Button(root, text='Merge and Save PDF: ', command=save_pdf, width=20, fg="red").grid(row=5, column=0, columnspan=4)

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

#To Update the Object after selecting the required Pages from the particluar PDF
# It shall update the written variable in start and end
start.trace('w',set_start)
end.trace('w',set_end)

root.mainloop()



