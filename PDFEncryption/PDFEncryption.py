from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import PyPDF2
import sys
#-------------------------------------------------------------------------------------------------
root = Tk()
#Global varialbe to hold the input PDF path
global_DocPath = ""
#Global varialbe to hold the output PDF path
global_EncryptFile = ""
#Varible to hold the entered password. It can be used inside the function without any GLOBAL declaration
strPassword = StringVar()
#-------------------------------------------------------------------------------------------------
def browsePDf():
    #Global Variable Syntax inside the function
    global global_DocPath
    global_DocPath = askopenfilename(filetypes=(('PDF Doc ', '*.PDF'), ('PDF', '*.PDF')))
    #Text box can be Editable.
    fileTextBox.config(state=NORMAL)
    fileTextBox.delete('1.0',END)
    fileTextBox.insert(END, global_DocPath.split('/')[-1])
    #Text box is Read Only. Write is disabled.
    fileTextBox.config(state=DISABLED)

#Error Handling after Clicking on SaveEncrypt Button
def SaveEncrypted():
    global global_DocPath
    if global_DocPath == "":
        messagebox.showerror("Error", "No PDF Selected for Encryption!")
    elif  strPassword.get() == "":
        messagebox.showerror("Error", "Enter the Password for Encryption")
    else:
        global global_EncryptFile
        global_EncryptFile = asksaveasfilename(filetypes=(('PDF Doc', '*.PDF'), ('PDF', '*.PDF')))
        if global_EncryptFile == "":
            pass
        else:
            fun_Encryption()

def fun_Encryption():
    try:
        global global_EncryptFile
        outputPdffile = global_EncryptFile + "_Encrypted.pdf"
        #Start Encryption
        pdfFile = open(global_DocPath, 'rb')
        # Create reader and writer object
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        # Add all pages to writer (accepted answer results into blank pages)
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        # Encrypt with your password
        pdfWriter.encrypt(strPassword.get())
        # Write it to an output file. (you can delete unencrypted version now)
        resultPdf = open(outputPdffile, 'wb')
        pdfWriter.write(resultPdf)
        messagebox.showinfo("File Saved","The File is saved at : "+outputPdffile )
        resultPdf.close()
    except:
        ex_msg = sys.exc_info()[0]
        messagebox.showerror("Exception", "Encryption Error:{0} and {1}".format(sys.exc_info()[0].__name__, sys.exc_info()[1]))

    root.quit()
#-------------------------------------------------------------------------------------------------
root.title("PDF Encryption")
Label(root, width= "25", text="PDF Encrypter").grid(row=0, column=3, columnspan=4)
Button(root, width="25", text="Browse and Add the PDF file", command = browsePDf, bg="lightblue").grid(row=1,column=1,columnspan=3)
fileTextBox = Text(root, width="25", height= "1",bg="grey90")
fileTextBox.grid(row=1, column=4,columnspan=6)
fileTextBox.config(state=DISABLED)

Label(root, width="25", text="Enter the Encryption Password").grid(row=2, column=1, columnspan=3)
Entry(root, textvariable = strPassword, width = "33").grid(row=2, column = 4, columnspan=6)

Button(root, width="20", text="Encrypt the PDF", command= SaveEncrypted, bg="lightblue").grid(row=3, column = 3, columnspan=4)

#-------------------------------------------------------------------------------------------------
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)
mainloop()

#-------------------------------------------------------------------------------------------------