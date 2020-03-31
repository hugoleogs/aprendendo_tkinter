from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Label 1')
lb1.grid(row=100, column=100)

lb2 = Label(janela, text='Label 2')
lb2.grid(row=2000, column=2000)




janela.geometry('500x200+-600+200')
janela.mainloop()