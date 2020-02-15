from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from nltk.corpus import stopwords 
from nltk import word_tokenize
import nltk
import string

class Text_Preprocesser():
    def __init__(self,master):
        self.master = master
        self.master.title("Text Preprocesser")
        self.master.geometry("250x150")
        self.master.resizable(False,False)
        self.filename = ""
        
        # menu
        self.menu = Menu(self.master)
        self.stop_words = set(stopwords.words('english'))
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a file" ,command = self.addf)
        self.file_menu.add_command(label = "Close a file",state="disable",command = self.closef)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu(self.menu,tearoff = 0)
        self.edit_menu.add_command(label = "Remove stop words")
        self.edit_menu.add_command(label = "Remove punctuation")
        self.edit_menu.add_command(label = "Word counter and distribution")
        self.menu.add_cascade(label = "Edit", menu = self.edit_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())

        #buttons
        self.remsstop = Button(self.master, text = "REMOVE STOP WORDS",command = self.stopw ,state="disable")
        self.remsstop.pack()

        self.rempun  = Button(self.master, text = "REMOVE PUNCTUATION",command = self.rempun , state="disable")
        self.rempun.pack()

        self.wordcanddist = Button(self.master, text = "WORD COUNTER AND DISTRIBUTION",command = self.wcd,state = "disable")
        self.wordcanddist.pack()
    
    def closef(self):
        """ closes file """
        self.filename = ""
        self.rempun.configure(state="disable")
        self.wordcanddist.configure(state = "disable")
        self.remsstop.configure(state  = "disable")
        self.file_menu.entryconfig("Close a file",state = "disable")
        self.file_menu.entryconfig("Insert a file",state = "active")
        msg.showinfo("CLOSE", "FILE SUCCESSFULLY CLOSED")
    
    def wcd(self):
        """ prints the number of words and the words distribution"""
        file  = open(str(self.filename),'r')
        line =file.read()
        token = word_tokenize(line)
        fdist = nltk.FreqDist(token)
        msg.showinfo("WORD COUNTER AND WORD DISTRIBUTION", "WORDS:" + str(len(token)) + "DISTRIBUTION" + str(fdist.most_common()) )
    
    def rempun(self):
        """ removes every kind of punctuation """
        remove = dict.fromkeys(map(ord, '\n ' + string.punctuation))
        file = open(str(self.filename),'r') 
        line = file.read()
        self.filenamesave2 =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        if ".txt" in self.filenamesave2:
            for r in line:
                if r not in string.punctuation:
                    appendFile = open(str(self.filenamesave2)+".txt",'a') 
                    appendFile.write(r) 
                    appendFile.close()
            msg.showinfo("SUCCESS","PUNCTUATION REMOVED SUCCESSFULLY")
        else:
            msg.showerror("Abort","Abort")
   
    
    def addf(self):
        """ inserts a .txt file and activates the buttons"""
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select txt file",
                                                   filetypes=(("txt files","*.txt"),("all files","*.*")))
        if ".txt" in self.filename:
            msg.showinfo("SUCCESS","TXT FILE ADDED SUCCESSFULLY")
            self.rempun.configure(state="active")
            self.wordcanddist.configure(state = "active")
            self.remsstop.configure(state  = "active")
            self.file_menu.entryconfig("Insert a file",state = "disable")
            self.file_menu.entryconfig("Close a file",state = "active")
        else:
            msg.showerror("ERROR" ,"NO TXT FILE ADDED ") 


    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()

    def stopw(self):
        """ removes stop words"""
        file1 = open(str(self.filename),'r') 
        line = file1.read()
        words = line.split() 
        self.filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        if ".txt" in self.filenamesave:
            for r in words: 
                if not r in self.stop_words: 
                    appendFile = open(str(self.filenamesave)+".txt",'a') 
                    appendFile.write(r) 
                    appendFile.close()
            msg.showinfo("SUCCESS","STOP WORDS REMOVED SUCCESSFULLY")
        else:
            msg.showerror("Abort","Abort")
            

    
    def helpmenu(self):
        msg.showinfo("Help", "Insert a .txt file and use the buttons to preprocess it")
    
    def aboutmenu(self):
        msg.showinfo("About", "Version 1.0")

        

def main():
    root=Tk()
    tp = Text_Preprocesser(root)
    root.mainloop()
    
if __name__=='__main__':
    main()