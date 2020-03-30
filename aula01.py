from tkinter import *

janela = Tk()
janela.title('PROGRAM DE TESTE')#Muda o titlo
janela.configure(bg='blue')#Cor de fundo
#janela.geometry('450x400+750+300')#larguraXaltura+posicaoX+posicaoY
#janela.resizable(False, False)#bloqueia o redimensionamento x and y
janela.iconphoto(True, PhotoImage(file='2.png'))#coloca um icone

#Objetivo abrir aplicacão do tamanho da tela
lateral = (janela.winfo_screenwidth())
altura = (janela.winfo_screenheight())
janela.geometry('%dx%d+0+0' % (lateral, altura))

janela.mainloop()