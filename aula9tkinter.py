from tkinter import *

def soma():
    if (str(ent.get()).isnumeric() and str(ent2.get()).isnumeric()):
        lb['text']= int(ent.get())+int(ent2.get())
    else:
        lb['text']= 'Valores informados invalidos!'

janela = Tk()

ent = Entry(janela)
ent.place(x=70, y=100)

ent2 = Entry(janela)
ent2.place(x=70, y=130)

bt1 = Button(janela, width= 17, text='SOMA ', command=soma)
bt1.place(x=70, y=160)

lb = Label(janela, text = 'saida')
lb.place(x=70, y=210)

janela.geometry('300x300+200+200')
janela.mainloop()