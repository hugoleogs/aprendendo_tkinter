from tkinter import *

janela = Tk()

lb1 = Label(janela, text='ESPACO', width='13', height=3, bg='blue')
lbHORIZONTAL = Label(janela, text='horizontal', bg='yellow')
lbVERTICAL = Label(janela, text='vertical', bg='yellow')

lb1.grid(row=0, column=0)
lbHORIZONTAL.grid(row=1, column=0, sticky=W)
lbVERTICAL.grid(row=0, column=1, sticky=N)




janela.geometry('200x100+100+100')
janela.mainloop()