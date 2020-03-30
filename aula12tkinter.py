from tkinter import *

janela = Tk()

lb1 = Label(janela, text='side1', bg='white')
lb2 = Label(janela, text='side2', bg='red')
lb3 = Label(janela, text='ANCHOR1', bg='white')
lb4 = Label(janela, text='ANCHOR2', bg='red')

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(side=BOTTOM, anchor=SW)

janela['bg']='black'
janela.geometry('400x300+200+200')
janela.mainloop()