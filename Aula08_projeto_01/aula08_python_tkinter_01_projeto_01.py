import mysql.connector
import os
from dotenv import load_dotenv
from cores import *
from tkinter import *
from tkinter import messagebox

load_dotenv('/.env')


def entrar():
    try:
        conn = mysql.connector.connect(host=os.environ['HOST'],
                                       port=os.environ['PORT'],
                                       user=campo_nome.get(),
                                       passwd=campo_passwd.get(),
                                       db=os.environ['DB'])
    except:
        messagebox.showerror('Erro', 'Erro ao conectar!')
    else:
        messagebox.showinfo('Sucesso', 'Conexão realizada com sucesso!')
    finally:
        campo_nome.delete(0, 'END')
        campo_passwd.delete(0, 'END')
        campo_nome.focus()


def mostrar_senha():
    if mostrar.get() == 1:
        campo_passwd['show'] = ''
    else:
        campo_passwd['show'] = '*'


# Criando a janela
janela = Tk()
janela.title('Tkinter - Projeto 01')
janela.geometry('300x220')
janela.configure(background=cor_fundo)
janela.resizable(width=False, height=False)
janela.bind('<Return>', entrar)

# Dividindo a janela
frame_cima = Frame(master=janela,
                   width=310,
                   height=50,
                   bg=cor_fundo)
frame_cima.grid(row=0,
                column=0,
                padx=0,
                pady=1,
                sticky=NSEW)

frame_baixo = Frame(master=janela,
                    width=310,
                    height=250,
                    bg=cor_fundo)
frame_baixo.grid(row=1,
                 column=0,
                 padx=0,
                 pady=1,
                 sticky=NSEW)

# Configurando frame_cima
label = Label(master=frame_cima,
              text='Login',
              font=('Arial', 25),
              fg=cor_letra,
              bg=cor_fundo)
label.place(x=5, y=3)

linha = Label(master=frame_cima,
              width=275,
              bg=cor_in)
linha.place(x=20, y=47)

# Configurando frame_baixo
nome = Label(master=frame_baixo,
             text='Nome',
             font=('Arial', 12),
             fg=cor_letra,
             bg=cor_fundo)
nome.place(x=10, y=20)

campo_nome = Entry(master=frame_baixo,
                   width=22,
                   justify='left',
                   font=('Arial', 12),
                   highlightthickness=1,
                   relief='solid')
campo_nome.place(x=60, y=20)

passwd = Label(master=frame_baixo,
               text='Senha',
               font=('Arial', 12),
               fg=cor_letra,
               bg=cor_fundo)
passwd.place(x=10, y=50)

campo_passwd = Entry(master=frame_baixo,
                     width=22,
                     justify='left',
                     show='*',
                     font=('Arial', 12),
                     highlightthickness=1,
                     relief='solid')
campo_passwd.place(x=60, y=50)

mostrar = IntVar()
check = Checkbutton(master=frame_baixo,
                    text='Mostrar senha',
                    variable=mostrar,
                    fg=cor_letra,
                    bg=cor_fundo,
                    activebackground=cor_fundo,
                    command=mostrar_senha)
check.place(x=60, y=80)

btn_confirmar = Button(master=frame_baixo,
                       text='ENTRAR',
                       font=('Arial', 10),
                       width=28,
                       # highlightthickness=20,
                       fg=cor_letra,
                       bg=cor_in,
                       activebackground=cor_in,
                       activeforeground=cor_fundo)
btn_confirmar.place(x=30, y=110)

# Dando foco ao campo Nome
campo_nome.focus()

if __name__ == '__main__':
    janela.mainloop()
