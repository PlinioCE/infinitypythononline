from tkinter import *
from tkinter import filedialog

lista_telefone = []


def cadastrar_contato():
    if field_telefone.get() not in lista_telefone:
        lista_telefone.append(field_telefone.get())
        arquivo_cadastro = filedialog.asksaveasfile(initialdir='C:\\Users\\Plinio\\Desktop',
                                                    title='Salvar arquivo',
                                                    defaultextension='.txt',
                                                    filetypes=[('Arquivo de texto', '.txt')])

        arquivo_nome = str(field_nome.get())
        arquivo_telefone = str(field_telefone.get())
        arquivo_cadastro.write(f'Nome: {arquivo_nome}\nTelefone: {arquivo_telefone}')
        arquivo_cadastro.close()
    else:
        alertar()


def alertar():
    alerta = Tk()
    alerta.title('ERRO')
    alerta.geometry('400x200')
    pop_alerta = Label(master=alerta, text='CONTATO EXISTENTE!', font=('Arial', 16), foreground='red')
    pop_alerta.place(x=90, y=80)
    alerta.mainloop()


janela = Tk()

janela.title('Cadastro Contato')
janela.geometry('600x260')
cabecalho = Label(text='Lista Telefônica', font=('Arial', 24, 'bold'))
cabecalho.place(x=190, y=10)

lbl_nome = Label(text='Nome: ', font=('Arial', 16))
lbl_nome.place(x=30, y=70)

field_nome = Entry(master=janela, font=('Arial', 14))
field_nome.place(x=130, y=72, relheight=0.11, relwidth=0.70)

lbl_telefone = Label(text='Telefone: ', font=('Arial', 16))
lbl_telefone.place(x=30, y=130)

field_telefone = Entry(master=janela, font=('Arial', 14))
field_telefone.place(x=130, y=132, relheight=0.11, relwidth=0.70)

btn_cadastro = Button(master=janela, text='Cadastrar', command=cadastrar_contato, font=('Arial', 16))
btn_cadastro.place(x=440, y=192)

if __name__ == '__main__':
    janela.mainloop()
