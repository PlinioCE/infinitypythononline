from tkinter import *


def saudacao(event=None):
    label2['text'] = f'Olá, {field1.get().title()}'
    field1.delete(0, 'end')


window = Tk()
window.title('Atividade de Aula')
window.bind('<Return>', saudacao)

label1 = Label(master=window, text='Digite seu nome: ', font=('Quicksand Regular', 14))
label1.grid(row=0, column=0, padx=5, pady=5)

field1 = Entry(master=window, font=('Quicksand Regular', 14))
field1.grid(row=0, column=1, padx=5, pady=5)
field1.focus()

btn1 = Button(master=window, text='Saudar', font=('Quicksand Regular', 14), command=saudacao)
btn1.grid(row=0, column=2, padx=5, pady=5)

btn2 = Button(master=window, text='Sair', font=('Quicksand', 14), command=exit)
btn2.grid(row=1, column=2, sticky=EW, padx=5, pady=5)

label2 = Label(master=window, text='', font=('Quicksand', 14))
label2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

if __name__ == '__main__':
    window.mainloop()
