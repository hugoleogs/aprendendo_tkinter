from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Login: ')
lb1.grid(row=1, column=1)

lb2 = Label(janela, text='Senha: ')
lb2.grid(row=2, column=1)

en1 = Entry(janela)
en1.grid(row=1, column=2)

en2 = Entry(janela)
en2.grid(row=2, column=2)

bt = Button(janela, width=12, text='Confirmar')
bt.grid(row=3, column=2)


janela.geometry('250x100+-600+200')
janela.mainloop()