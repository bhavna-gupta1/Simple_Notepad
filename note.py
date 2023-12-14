import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
import os

# FUNCTION FOR ALL MENU ITEMS
def newfile():
    global textArea
    root.title('Untitled Notepad')
    file = NONE
    textArea.delete(1.0,END)

def openfile():
   global textArea
   file = filedialog.askopenfile(defaultextension='txt',filetypes=[('All Files','*.*'),('Text Document','*.txt')])
   file = file.name

   if file=='':
       file = None
   else:
       root.title(os.path.basename(file)+' - Note')
       textArea.delete(1.0,END)
       file=open(file,'rb')
       textArea.insert(1.0,file.read())
       file.close()

def savefile():
    global textArea,file
    if file==None:
        file= filedialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension='txt',filetypes=[('All Files','*.*'),('Text Document','*.txt')])
        if file == None:
            file=None
        else:
            file=open(file,'w')
            file.write(textArea.get(1.0,END))
            file.close()
            file=file.nameroot=(os.path.basename(file) + ' - Notepad')
    else:
        file=open(file,'w')
        file.write(textArea.get(1.0,END))
        file.close()

def exit():
    root.destroy()

def cut():
    global textArea
    textArea.event_generate('<<Cut>>')
def copy():
    global textArea
    textArea.event_generate('<<Copy>>')

def paste():
    global textArea
    textArea.event_generate('<<Paste>>')

def help():
    messagebox.showinfo('Notepad','This simple Notepad is developed by me..!!')

root= tk.Tk()
root.title('Untitled Notepad')
file=None


def createWidgets():
    global textArea
    textArea=Text(root)
    textArea.grid(sticky=N+W+S+E) 
    # MENU FOR FILE
    menu_bar= Menu(root)
    root.config(menu=menu_bar)
    fileMenu=Menu(menu_bar,tearoff=0)
    fileMenu.add_command(label='New',command=newfile) 
    fileMenu.add_command(label='open',command= openfile)
    fileMenu.add_command(label='save',command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit',command=exit)
    menu_bar.add_cascade(label='File',menu=fileMenu)
     
    # MENU FOR 
    editMenu=Menu(menu_bar,tearoff=0)
    editMenu.add_command(label='Cut',command=cut) 
    editMenu.add_command(label='Copy',command=copy)
    editMenu.add_command(label='Paste',command=paste)
    menu_bar.add_cascade(label='Edit',menu=editMenu)

    # MENU FOR HELP
    helpMenu=Menu(menu_bar,tearoff=0)
    helpMenu.add_command(label='About Notepad',command=help)
    menu_bar.add_cascade(label='Help',menu=helpMenu)


       

createWidgets()
root.mainloop()