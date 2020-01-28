from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
from nltk.corpus import stopwords 
import re

class Text_Preprocesser():
    def __init__(self,master):
        self.master = master
        self.master.title("Text Preprocesser")
        self.master.geometry("250x150")
        self.master.resizable(False,False)

        
        
        self.menu = Menu(self.master)
        self.stop_words = set(stopwords.words('english'))
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert a file" ,command = self.addf)
        self.file_menu.add_command(label = "Save a file",state="disable")
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
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

        self.remsstop = Button(self.master, text = "REMOVE STOP WORDS",command = self.stopw ,state="disable")
        self.remsstop.pack()

        self.rempun  = Button(self.master, text = "REMOVE PUNCTUATION",command = self.rempun , state="disable")
        self.rempun.pack()
    
    def rempun(self):
        pass
    
    def addf(self):
         self.filename = filedialog.askopenfilename(initialdir="/",title="Select txt file",
                                                   filetypes=(("txt files","*.txt"),("all files","*.*")))
         if ".txt" in self.filename:
             msg.showinfo("SUCCESS","THE TXT FILE ADDED SUCCESSFULLY")
             self.rempun.configure(state="active")
             self.remsstop.configure(state  = "active")
             self.file_menu.entryconfig("Insert a file",state = "disable")
         else:
             msg.showerror("ERROR" ,"NO TXT FILE ADDED ") 


    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()

    def stopw(self):
        file1 = open(str(self.filename),'r') 
        line = file1.read()
        words = line.split() 
        self.filenamesave =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        if "*.txt" in self.filenamesave:
            for r in words: 
                if not r in self.stop_words: 
                    appendFile = open(str(self.filenamesave)+".txt",'a') 
                    appendFile.write(" "+r) 
                    appendFile.close()
        else:
            msg.showerror("Abort","Abort")
            

    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

        

def main():
    root=Tk()
    tp = Text_Preprocesser(root)
    root.mainloop()
    
if __name__=='__main__':
    main()