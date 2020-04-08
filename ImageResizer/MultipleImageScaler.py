#With GUI Support. Input the Image and enter the value to rescale the image.
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image

#-------------------------------------------------------------------------------------------------
root = Tk()
root.title("Image Size Reducer")

#List to hold the list of Images
image_list = []
strScaleValue = StringVar()
#Global variable to hold the output directory
global_outputFolder = ""
#-------------------------------------------------------------------------------------------------
def browseImage():
    imageFiles = askopenfilenames(filetypes=(('Image File ', '*.JPEG *.JPG *.PNG *.GIF'), ('Other formats', '*.TIFF *.BMP')))
    for image in imageFiles:
        image_list.append(image)
        listbox.insert(END, image.split('/')[-1])

def setOutDir():
    global global_outputFolder
    global_outputFolder = askdirectory()

def resizeImage():
    try:
        if len(image_list) == 0:
            messagebox.showerror("Error", "No Image file found!")
        elif  (strScaleValue.get() == "" or int(strScaleValue.get()) < 5 or int(strScaleValue.get()) > 100):
            messagebox.showerror("Error", "Enter the Resize value between 5 and 100")
        else:
            global global_outputFolder
            if global_outputFolder == "":
                messagebox.showerror("Error", "Output Folder not Set!")
            else:
                fun_Resize()
    except:
        messagebox.showerror("Exception", "Error:{0} and {1}".format(sys.exc_info()[0].__name__, sys.exc_info()[1]))

def fun_Resize():
    for image in image_list:
        outputImagefile = global_outputFolder + '/'+ "Resize_" + image.split('/')[-1]
        #Image below is imported from PIL library
        imagePath = Image.open(image)
        imagePath.save(outputImagefile,optimize=True,quality=int(strScaleValue.get()))
        imagePath.close()
    messagebox.showinfo("Files Saved","All the scaled files are saved at : "+global_outputFolder )
    root.quit()
#-------------------------------------------------------------------------------------------------
Label(root, width= "20", text="IMAGE SCALER").grid(row=0, column=1, columnspan=4)
Button(root, width="25", height="2",text="Browse and Add Image file", command = browseImage, bg="lightblue").grid(row=1,column=0,columnspan=2)

listbox = Listbox(root, width="30", height="20")
listbox.bind('<<ListboxSelect>>')
listbox.grid(row=2, rowspan=4, column=0, columnspan=2)

Button(root, width="20", height="2",text="Set Output Folder", command = setOutDir).grid(row=1,column=3,columnspan=4)
Label(root, width="40",  wraplength="150",text="Enter Value to Resize.\n (Between 5 & 100).\n"
      "5-> Lesser Size/Poor Quality.\n 100-> Higher size/Good Quality.").grid(row=2, rowspan=2,column=3, columnspan=4, sticky="n,s,e,w")

Entry(root, textvariable = strScaleValue, width="23").grid(row=3, column = 3, columnspan=5, sticky="s")

Button(root, width="20", height="2", text="Resize Images", command= resizeImage, bg="lightblue").grid(row=5, column = 3, columnspan=5)
#-------------------------------------------------------------------------------------------------

for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)
mainloop()
