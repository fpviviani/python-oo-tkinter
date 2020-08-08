import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereAluno(tk.Toplevel):

    def __init__(self, controle, listaCursos):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Aluno")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro, text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso,text="Escolha o curso: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCurso.pack(side="left")

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="right")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="right")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        type = "insere"
        self.buttonSubmit.bind("<Button-1>", lambda event, arg=type: controle.enterHandler(event, type))

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button-1>", lambda event, arg=type: controle.clearHandler(event, type))

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button-1>", lambda event, arg=type: controle.fechaHandler(event, type))

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)