import pickle
import pandas as pd
from tkinter import *
from tkinter import ttk
from nltk.tokenize import word_tokenize

with open('./model.pkl', 'rb') as file:
    model = pickle.load(file, errors='ignore')

dis_df = pd.read_csv('./data.csv', index_col='disease')

df = pd.read_csv("./symptoms-weight.csv", index_col='Disease')
sympts = df.columns.tolist()

sevrty = pd.read_csv("Symptom-severity.csv", index_col="Symptom")


def predict(data: list):

    lst = pd.DataFrame(data).transpose()
    col = df.columns.tolist()
    lst.columns = col
    data = lst

    prediction = model.predict(data)[0]

    return prediction


def weightadder(sen):

    filtered_list = word_tokenize(sen)

    lst = []

    for i in sympts:
        s_symp = i.split("_")
        present = True

        for s in s_symp:
            if s not in filtered_list:
                present = False
                break

        if present:
            weight = sevrty.loc[i, "weight"]
            lst.append(weight)
        else:
            lst.append(0)

    return lst


def add_symptom():
    sympt = sympt_list.get(sympt_list.curselection())
    txt.insert(END, sympt+" ")


def clear_txt():
    txt.delete('1.0', END)


def predict_dis():
    sen = txt.get("1.0", END)
    input_sympts_lst = weightadder(sen)
    disease = predict(input_sympts_lst)

    dis_name.config(state='normal')
    dis_name.delete("1.0", END)
    dis_name.insert("1.0", disease)
    dis_name.config(state='disabled')

    out = dis_df.loc[disease]

    about_dis.config(state='normal')
    about_dis.delete("1.0", END)
    about_dis.insert("1.0", 'Discription :\n\n')
    about_dis.insert("3.0", out['discription'])
    about_dis.config(state='disabled')

    precautions = out['precautions'].split(",")

    precau.config(state='normal')
    precau.delete("1.0", END)
    precau.insert("1.0", "Precautions :\n\n")
    for i, preco in enumerate(precautions):
        precau.insert(str(2*i+3)+".0", str(i+1) + ") " + preco.lstrip()+"\n\n")
    precau.config(state='disabled')


if __name__ == "__main__":

    root = Tk()

    root.attributes("-fullscreen", True)

    content = ttk.Frame(root, padding=(10, 10, 10, 10))
    frame = Frame(content, borderwidth=4,
                  relief="ridge", width=1710, height=955)

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

    do_predict = Button(content, text="Image", image=button_img,
                        command=predict_dis, width=915, height=230)

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
    do_predict.grid(column=2, row=1, columnspan=2)
    dis_name.grid(column=2, row=2, columnspan=2)
    about_dis.grid(column=2, row=3, rowspan=3)
    precau.grid(column=3, row=3, rowspan=3)

    content.grid(column=0, row=0)

    root.mainloop()
