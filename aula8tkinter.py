from tkinter import *

def bt_onclick():

    lb['text'] = ed.get()



janela = Tk()

ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=17, text='Enviar', command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(janela, text='Saída')
lb.place(x=100, y=200)

janela.geometry('300x300+300+300')
janela.mainloop()