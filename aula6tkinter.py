from tkinter import *

janela = Tk()

def bt_click():
    print("bt_click")
    label["text"] = "Deus_Seja_Louvado!"

bt = Button(janela, width=10, text='OK', command=bt_click)
bt.place(x=100, y=100)

label= Label(janela, text = 'Deus_eh_fiel')
label.place(x=80, y=150)





janela.geometry("300x300+200+200")
janela.mainloop()