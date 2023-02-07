from tkinter import *

window = Tk()

txt = Label(text='Infinity School', foreground='red', background='white', font='Bold')
# txt = Label(text='Infinity School', foreground='#C64132', background='#FFFFFF')
txt.pack(fill=X)

btn = Button(text='Clique aqui', width=25, height=5, fg='#FFFFFF', bg='#0D0052')
btn.pack()

nome = Label(text='Nome: ')
campo = Entry(fg='#2A2A2A', bg='#F3E8E8', width=30)
nome.pack()
# campo.get()
# campo.delete()
# campo.insert()
campo.pack()

fr1 = Frame(master=window, width=100, height=100, bg='red')
fr1.pack(fill=X)

fr2 = Frame(master=window, width=50, height=50, bg='yellow')
fr2.pack(fill=Y)

fr3 = Frame(master=window, width=25, height=25, bg='blue')
fr3.pack(fill=BOTH)

window.mainloop()
