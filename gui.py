from tkinter import *
from tkinter import ttk
import pandas as pd
from main import predict

sympts = pd.read_csv("./symptoms-weight.csv", index_col='Disease')
sympts = sympts.columns.tolist()


def add_symptom():
    sympt = sympt_list.get(sympt_list.curselection())
    txt.insert(END, sympt+" ")


def clear_txt():
    txt.delete('1.0', END)


root = Tk()

content = ttk.Frame(root, padding=(10, 10, 10, 10))
frame = Frame(content, borderwidth=4, relief="ridge", width=1710, height=955)

button_img = PhotoImage(file="button_img.png")

title = Label(content, text="Disease Pridiction Bot",
              width=188, height=3, background="grey")

about = Label(content, text="This is about our project",
              width=95, height=10)

speak = Button(content, text="press to speak",
               width=45, height=19)

add_sympt = Button(content, text="Add Symptom",
                   command=add_symptom, width=43, height=3)

var2 = StringVar()
var2.set(sympts)
sympt_list = Listbox(content, listvariable=var2, width=46, height=15)

txt = Text(content, width=95, height=7)

clear = Button(content, text="clear", command=clear_txt, width=92)

img = Button(content, text="Image", image=button_img, width=915, height=230)

dis_name = Text(content, width=91, height=3)
dis_name.insert("1.0", "Disease Name")
dis_name.config(state='disabled')

about_dis = Text(content, width=45, height=25)
about_dis.insert("1.0", "About Disease")
about_dis.config(state='disabled')

precau = Text(content, width=45, height=25)
precau.insert("1.0", "Precaution of Disease")
precau.config(state='disabled')


title.grid(column=0, row=0, columnspan=4)
about.grid(column=0, row=1, columnspan=2)
speak.grid(column=0, row=2, rowspan=2)
add_sympt.grid(column=1, row=2)
sympt_list.grid(column=1, row=3)
txt.grid(column=0, row=4, columnspan=2)
clear.grid(column=0, row=5, columnspan=2)
img.grid(column=2, row=1, columnspan=2)
dis_name.grid(column=2, row=2, columnspan=2)
about_dis.grid(column=2, row=3, rowspan=3)
precau.grid(column=3, row=3, rowspan=3)

content.grid(column=0, row=0)

root.mainloop()
