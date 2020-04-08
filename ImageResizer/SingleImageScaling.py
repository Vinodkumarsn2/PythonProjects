#With GUI Support. Input the Image and enter the value to rescale the image.
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image

#-------------------------------------------------------------------------------------------------
root = Tk()
root.title("Image Size Reducer")
strScaleValue = StringVar()
#Global varialbe to hold the input Image path
global_DocPath = ""
#Global varialbe to hold the output Resized Image
global_ResizedImage = ""
#-------------------------------------------------------------------------------------------------
def browseImage():
    #Global Variable Syntax inside the function
    global global_DocPath
    global_DocPath = askopenfilename(filetypes=(('Image File ', '*.JPEG *.JPG *.PNG *.GIF'), ('Other formats', '*.TIFF *.BMP')))
    #Text box can be Editable.
    fileTextBox.config(state=NORMAL)
    fileTextBox.delete('1.0',END)
    fileTextBox.insert(END, global_DocPath.split('/')[-1])
    #Text box is Read Only. Write is disabled.
    fileTextBox.config(state=DISABLED)

def resizeImage():
    global global_DocPath
    try:
        if global_DocPath == "":
            messagebox.showerror("Error", "No Image file Selected!")
        elif  (strScaleValue.get() == "" or int(strScaleValue.get()) < 5 or int(strScaleValue.get()) > 100):
            messagebox.showerror("Error", "Enter the Resize value between 5 and 100")
        else:
            global global_ResizedImage
            global_ResizedImage = asksaveasfilename(filetypes=(('Image File ', '*.JPEG *.JPG *.PNG *.GIF'),
                                                               ('Other formats', '*.TIFF *.BMP')))
            if global_ResizedImage == "":
                pass
            else:
                fun_Resize()
    except:
        messagebox.showerror("Exception", "Error:{0} and {1}".format(sys.exc_info()[0].__name__, sys.exc_info()[1]))

def fun_Resize():
    try:
        global global_ResizedImage
        outputImagefile = global_ResizedImage + "_Resized.JPEG"
        imagePath = Image.open(global_DocPath)
        imagePath.save(outputImagefile,optimize=True,quality=int(strScaleValue.get()))
        messagebox.showinfo("File Saved","The File is saved at : "+outputImagefile )
        imagePath.close()
    except:
        messagebox.showerror("Exception", "Resizing Error:{0} and {1}".format(sys.exc_info()[0].__name__, sys.exc_info()[1]))
    root.quit()
#-------------------------------------------------------------------------------------------------
Label(root, width= "25", text="Image Scaler").grid(row=0, column=3, columnspan=4)
Button(root, width="25", text="Browse and Add Image file", command = browseImage, bg="lightblue").grid(row=1,column=1,columnspan=3)
fileTextBox = Text(root, width="25", height= "1",bg="grey90")
fileTextBox.grid(row=1, column=4,columnspan=6)
fileTextBox.config(state=DISABLED)

Label(root, width="30",  wraplength="210",text="Enter Value to Resize(Between 5 & 100).")\
      .grid(row=2, column=1, columnspan=3)
Entry(root, textvariable = strScaleValue, width = "33").grid(row=2, column = 4, columnspan=6)
Label(root, width="25",height="-1", wraplength="180", text=" 5-> Lesser Size/Poor Quality. 100-> Higher size/Good Quality")\
      .grid(row=3, column=1, columnspan=3)

Button(root, width="20", text="Resize Image", command= resizeImage, bg="lightblue").grid(row=4, column = 3, columnspan=4)
#-------------------------------------------------------------------------------------------------

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)
mainloop()
