import glob
import pdf2image
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import os

img_size_factor = 3

class Gui:
    def __init__(self):
        # Data Variables
        self.inputName = ''
        self.pdfList = []
        self.currentDocument = ''
        # GUI elements
        self.inputRename = None
        self.buttonCommit = None
        self.labelRename = None
        # GUI init
        self.root = tkinter.Tk()
        self.root.bind('<Return>', self.onButtonRename)
    def scanFiles(self, pattern):
        self.pdfList = glob.glob(str(pattern))
    def onButtonRename(self, *args):
        newFilename=self.inputRename.get()
        for widget in self.root.winfo_children(): widget.destroy()
        rename_file(self.currentDocument, newFilename)
        self.showAndRename()
    def showAndRename(self):
        if len(self.pdfList) == 0:
            messagebox.showinfo("Information","No more PDFs to rename.")
            self.root.destroy()
            return
        self.currentDocument = self.pdfList.pop()
        img = pdf_to_img(self.currentDocument)
        self.showImage(img)
        self.labelRename = tkinter.Label(self.root, text="Old filename:\n" + str(self.currentDocument) + "\n\nNew filename:")
        self.inputRename = tkinter.Entry(self.root, width=40)
        self.inputRename.insert('end', str(self.currentDocument))
        self.inputRename.selection_range(0, 'end')
        self.inputRename.focus_set()
        self.buttonCommit=tkinter.Button(self.root, height=1, width=10, text="Rename",
            command=lambda: self.onButtonRename())
        self.labelRename.pack()
        self.inputRename.pack()
        self.buttonCommit.pack()
    def showImage(self, img):
        global img_size_factor
        img = img.resize((210*img_size_factor, 297*img_size_factor), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.root, image=img)
        panel.image = img
        panel.pack()
    def loop(self):
        self.root.mainloop()

def pdf_to_img(pdf_file):
    # Create preview image of first page of PDF
    return pdf2image.convert_from_path(pdf_file, dpi=75, last_page=1)[0]

def rename_file(old_name, new_name):
    if old_name == new_name: return
    if len(new_name) > 3:
        if new_name[-4:] == '.pdf':
            os.rename(old_name, new_name)
            return
    os.rename(old_name, str(new_name) + '.pdf')

'''
def show_path_selection():
    tkinter.Label(root, text="Please enter search path").pack()
'''