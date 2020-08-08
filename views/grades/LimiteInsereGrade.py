import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereGrade(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaCursos):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Grade")
        self.controle = controle

        self.frameAno = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAno.pack()
        self.frameCurso.pack()
        self.frameDiscip.pack()
        self.frameButton.pack()        

        self.labelAno = tk.Label(self.frameAno,text="Informe o ano da grade: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.labelCurso = tk.Label(self.frameCurso,text="Escolha o curso: ")
        self.labelCurso.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.listbox = tk.Listbox(self.frameDiscip)
        self.listbox.pack(side="left")
          
        for cod in listaCodDiscip:
            self.listbox.insert(tk.END, cod)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Disciplina")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereDisciplina)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Grade")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaGrade)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)   