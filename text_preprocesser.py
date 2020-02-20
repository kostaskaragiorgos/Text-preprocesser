from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
import string
from nltk.corpus import stopwords 
from nltk import word_tokenize
import nltk
class TextPreprocesser():
    def __init__(self, master):
        self.master = master
        self.master.title("Text Preprocesser")
        self.master.geometry("250x150")
        self.master.resizable(False, False)
        self.filename = ""
		self.stop_words = set(stopwords.words('english'))
        # menu
        self.menu = Menu(self.master)
        #FILE MENU 
		self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file", command=self.addf)
        self.file_menu.add_command(label="Close a file", state="disable", command=self.closef)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
		#EDIT MENU
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Remove stop words", accelerator='Alt + R', command=self.stopw)
        self.edit_menu.add_command(label="Remove punctuation", accelerator='Alt + P', command=self.rempunf)
        self.edit_menu.add_command(label="Word counter and distribution", accelerator='Alt + W', command=self.wcd)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
		#ABOUT
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        #HELP
		self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        #keybinds
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())
        self.master.bind('<Alt-r>', lambda event: self.stopw())
        self.master.bind('<Alt-p>', lambda event: self.rempunf())
        self.master.bind('<Alt-w>', lambda event: self.wcd())
        #buttons
        self.remsstop = Button(self.master, text="REMOVE STOP WORDS", command=self.stopw, state="disable")
        self.remsstop.pack()
		#REMOVE PUNCTUATION
        self.rempun = Button(self.master, text="REMOVE PUNCTUATION", command=self.rempunf, state="disable")
        self.rempun.pack()
		#WORD COUNTER AND DISTRIBUTION
        self.wordcanddist = Button(self.master, text="WORD COUNTER AND DISTRIBUTION", command=self.wcd, state="disable")
        self.wordcanddist.pack()
    def closef(self):
        """ closes file """
        self.filename = ""
        self.rempun.configure(state="disable")
        self.wordcanddist.configure(state="disable")
        self.remsstop.configure(state="disable")
        self.file_menu.entryconfig("Close a file", state="disable")
        self.file_menu.entryconfig("Insert a file", state="active")
        msg.showinfo("CLOSE", "FILE SUCCESSFULLY CLOSED")
    def wcd(self):
        """ prints the number of words and the words distribution"""
        if self.filename == "":
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            file = open(str(self.filename), 'r')
            line = file.read()
            token = word_tokenize(line)
            fdist = nltk.FreqDist(token)
            msg.showinfo("WORD COUNTER AND WORD DISTRIBUTION", "WORDS:" + str(len(token)) + "DISTRIBUTION" + str(fdist.most_common()))
    def rempunf(self):
        """ removes every kind of punctuation """
        if self.filename == "":
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            remove = dict.fromkeys(map(ord, '\n ' + string.punctuation))
            file = open(str(self.filename), 'r') 
            line = file.read()
            self.filenamesave2 =  filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            if ".txt" in self.filenamesave2:
                for r in line:
                    if r not in string.punctuation:
                        append_file = open(str(self.filenamesave2)+".txt", 'a') 
                        append_file.write(r) 
                        append_file.write(r) 
                        append_file.close()
                msg.showinfo("SUCCESS", "PUNCTUATION REMOVED SUCCESSFULLY")
            else:
                msg.showerror("Abort", "Abort")
    def addf(self):
        """ inserts a .txt file and activates the buttons"""
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                 filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if ".txt" in self.filename:
            msg.showinfo("SUCCESS", "TXT FILE ADDED SUCCESSFULLY")
            self.rempun.configure(state="active")
            self.wordcanddist.configure(state="active")
            self.remsstop.configure(state="active")
            self.file_menu.entryconfig("Insert a file", state="disable")
            self.file_menu.entryconfig("Close a file", state="active")
        else:
            msg.showerror("ERROR", "NO TXT FILE ADDED ")
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def stopw(self):
        """ removes stop words"""
        if self.filename == "":
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            file1 = open(str(self.filename), 'r') 
            line = file1.read()
            words = line.split() 
            self.filenamesave =  filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            if ".txt" in self.filenamesave:
                for r in words: 
                    if not r in self.stop_words: 
                        append_file = open(str(self.filenamesave)+".txt", 'a') 
                        append_file.write(r) 
                        append_file.close()
                msg.showinfo("SUCCESS", "STOP WORDS REMOVED SUCCESSFULLY")
            else:
                msg.showerror("Abort", "Abort")
    def helpmenu(self):
        msg.showinfo("Help", "Insert a .txt file and use the buttons to preprocess it")
    def aboutmenu(self):
        msg.showinfo("About", "Version 1.0")
def main():
    root = Tk()
    tp = TextPreprocesser(root)
    root.mainloop() 
if __name__ == '__main__':
    main()