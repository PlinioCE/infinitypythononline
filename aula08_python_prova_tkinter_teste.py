from tkinter import *
from tkinter import filedialog


def salvar_arquivo():
    arquivo = filedialog.asksaveasfile(initialdir='C:\\Users\\Plinio\\Desktop',
                                       title='Salvar arquivo',
                                       defaultextension='.txt',
                                       filetypes=[('Arquivo de cabecalho', '.txt')])

    arquivo_texto = str(texto.get(1.0, END))
    arquivo.write(arquivo_texto)
    arquivo.close()


janela = Tk()
botao = Button(text='Cadastrar', command=salvar_arquivo)
botao.pack()
texto = Text(janela)
texto.pack()
janela.mainloop()
