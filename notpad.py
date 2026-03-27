# tikenter module and libary to make gui app
import tkinter as tk
from tkinter import filedialog, messagebox
root= tk.Tk()
root.title('welcome to text editor')
root.geometry('800x600')

#create text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=('helvetica',20)
)
text.pack(expand=True,fill=tk.BOTH)

#main ogic start 
# function for new file
def newfile():
    text.delete(1.0,tk.END)

# function to open new file
def openfile():
    filepath=filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes=[('Text Files','*.txt')]
    )

    if filepath:
        #open file
        with open(filepath,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())

# function 3 save the file
def savefile():
    filepath=filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text Files','*.txt')]
    )
    if filepath:
        with open(filepath,'w') as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo('info','file saved successfully')

#menu bar creation
menu=tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)

# new open save exit
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='open',command=openfile)
filemenu.add_command(label='save',command=savefile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
#starts and keep the window open
root.mainloop()

