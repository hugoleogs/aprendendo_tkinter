from tkinter import *

janela = Tk()

janela.geometry('500x640')
janela.resizable(False, False)

frametop = Frame(janela, width=500, height=120, bg='#d3d3d3', relief='groove', bd='5')
frametop.pack()

framemeio = Frame(janela, width=500, height=400, bg='#87ceeb')
framemeio.pack()

framerodape = Frame(janela, width=500, height=120, bg='#f5deb3', relief='ridge', bd='5' )
framerodape.pack()

janela.mainloop()
