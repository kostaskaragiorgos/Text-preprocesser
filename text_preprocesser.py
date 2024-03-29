"""
 text preprocesser
    You can remove stop words , punctuation from texts
    """
from tkinter import Tk, Menu, Button
from tkinter import messagebox as msg
from tkinter import filedialog
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
def file_save(filename, r):
    """ creates and saves the new file """
    append_file = open(str(filename)+".txt", 'a')
    append_file.write(r)
    append_file.write(r)
    append_file.close()
def showstopwordlan():
    """ shows the languages where stopwords are available """  
    msg.showinfo("STOP WORDS LANGUAGES", "ENGLISH")
def helpmenu():
    """ help menu function"""
    msg.showinfo("Help", "Insert a .txt file and use the buttons to preprocess it")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 1.0")
class TextPreprocesser():
    """
    Text Preprocesser class
     """
    def __init__(self, master):
        self.master = master
        self.master.title("Text Preprocesser")
        self.master.geometry("250x150")
        self.master.resizable(False, False)
        self.filename = ""
        self.stop_words = set(stopwords.words('english'))
        self.word_counter = 0
        # menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a file", accelerator='Ctrl+O', command=self.addf)
        self.file_menu.add_command(label="Close a file",
                                   accelerator='Ctrl+F5', state="disable", command=self.closef)
        self.file_menu.add_command(label="Create a report file", accelerator='Alt+F5' ,command=self.filereport)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Remove stop words",
                                   accelerator='Alt + R', command=self.stopw)
        self.edit_menu.add_command(label="Remove punctuation",
                                   accelerator='Alt + P', command=self.rempunf)
        self.edit_menu.add_command(label="Words to lower case",
                                   accelerator='Ctrl+L', command=self.wordlow)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Word counter and distribution",
                                   accelerator='Alt + W', command=self.wcd)
        self.show_menu.add_command(label="Available Stop Words Lan",
                                   accelerator='Ctrl + S', command=showstopwordlan)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        #keybinds
        self.master.config(menu=self.menu)
        self.master.bind('<Control-s>', lambda event: showstopwordlan())
        self.master.bind('<Control-o>', lambda event: self.addf())
        self.master.bind('<Control-F5>', lambda event: self.closef())
        self.master.bind('<Alt-F5>', lambda event: self.filereport())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-r>', lambda event: self.stopw())
        self.master.bind('<Alt-p>', lambda event: self.rempunf())
        self.master.bind('<Alt-w>', lambda event: self.wcd())
        self.master.bind('<Control-l>', lambda event: self.wordlow())
        #buttons
        self.remsstop = Button(self.master, text="REMOVE STOP WORDS",
                               command=self.stopw, state="disable")
        self.remsstop.pack()
		#REMOVE PUNCTUATION
        self.rempun = Button(self.master, text="REMOVE PUNCTUATION",
                             command=self.rempunf, state="disable")
        self.rempun.pack()
		#WORD COUNTER AND DISTRIBUTION
        self.wordcanddist = Button(self.master, text="WORD COUNTER AND DISTRIBUTION",
                                   command=self.wcd, state="disable")
        self.wordcanddist.pack()
        self.wordstolower = Button(self.master, text="WORDS TO LOWER CASE",
                                   command=self.wordlow, state="disable")
        self.wordstolower.pack()

    def filereport(self):
        """
        creates a .txt file report of the inserted .txt file
        """
        if self.filename == "":
            msg.showerror("ERROR", "NO .TXT FILE.\nINSERT A .TXT FILE TO CREATE A REPORT")
        else:
            report = open("report.txt", 'w')
            report.write("The total number of words of the file are:" + str(self.word_counter))
            report.close()


    def closef(self):
        """ closes file """
        if  self.filename == "":
            msg.showerror("ERROR", "NO .TXT FILE TO CLOSE")
        else:
            self.filename = ""
            self.wordstolower.configure(state="disable")
            self.rempun.configure(state="disable")
            self.wordcanddist.configure(state="disable")
            self.remsstop.configure(state="disable")
            self.file_menu.entryconfig("Close a file", state="disable")
            self.file_menu.entryconfig("Insert a file", state="active")
            msg.showinfo("CLOSE", "FILE SUCCESSFULLY CLOSED")
    def wordlow(self):
        """ converts to lowercase"""
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            file1 = open(str(self.filename), 'r') 
            line = file1.read()
            words = line.lower()
            self.filenamesave = filedialog.asksaveasfilename(initialdir="/",
                                                             title="Select file",
                                                             filetypes=(("txt files", "*.txt"),
                                                                        ("all files", "*.*")))
            if ".txt" in self.filenamesave:
                for r in words:
                    file_save(self.filenamesave, r)
                msg.showinfo("SUCCESS",
                             "WORDS CONVERTED TO LOWER CASE SUCCESSFULLY")
            else:
                msg.showerror("Abort", "Abort")
    def wcd(self):
        """ prints the number of words and the words distribution"""
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            file = open(str(self.filename), 'r')
            line = file.read()
            token = word_tokenize(line)
            self.wordcounter = len(token)
            fdist = nltk.FreqDist(token)
            msg.showinfo("WORD COUNTER AND WORD DISTRIBUTION",
                         "WORDS:" + str(self.wordcounter) + 
                         "DISTRIBUTION" + str(fdist.most_common()))
    def stopw(self):
        """ removes stop words"""
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            file1 = open(str(self.filename), 'r') 
            line = file1.read()
            words = line.split() 
            self.filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                             filetypes=(("txt files", "*.txt"),
                                                                        ("all files", "*.*")))
            if ".txt" in self.filenamesave:
                for r in words: 
                    if not r in self.stop_words:
                        file_save(self.filenamesave, r)
                msg.showinfo("SUCCESS", "STOP WORDS REMOVED SUCCESSFULLY")
            else:
                msg.showerror("Abort", "Abort")
    def rempunf(self):
        """ removes every kind of punctuation """
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "IMPORT A .TXT FILE")
        else:
            dict.fromkeys(map(ord, '\n ' + string.punctuation))
            file = open(str(self.filename), 'r') 
            line = file.read()
            self.filenamesave2 = filedialog.asksaveasfilename(initialdir="/",
                                                              title="Select file",
                                                              filetypes=(("txt files", "*.txt"),
                                                                         ("all files", "*.*")))
            if ".txt" in self.filenamesave2:
                for r in line:
                    if r not in string.punctuation:
                        file_save(self.filenamesave2, r)
                msg.showinfo("SUCCESS", "PUNCTUATION REMOVED SUCCESSFULLY")
            else:
                msg.showerror("Abort", "Abort")
    def menuchange(self):
        """ changes the state of  menus """
        self.rempun.configure(state="active")
        self.wordcanddist.configure(state="active")
        self.remsstop.configure(state="active")
        self.wordstolower.configure(state="active")
        self.file_menu.entryconfig("Insert a file", state="disable")
        self.file_menu.entryconfig("Close a file", state="active")

    def addf(self):
        """ inserts a .txt file and activates the buttons"""
        if not self.filename == "":
            msg.showerror("ERROR", "FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                       filetypes=(("txt files", "*.txt"),
                                                                  ("all files", "*.*")))
            if ".txt" in self.filename:
                msg.showinfo("SUCCESS", "TXT FILE ADDED SUCCESSFULLY")
                self.menuchange()
            else:
                self.filename == ""
                msg.showerror("ERROR", "NO TXT FILE ADDED ")
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """ 
    root = Tk()
    TextPreprocesser(root)
    root.mainloop()
if __name__ == '__main__':
    main()
