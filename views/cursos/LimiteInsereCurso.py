import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x50')
        self.title("Curso")
        self.controle = controle

        self.frameNomeCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNomeCurso.pack()
        self.frameButton.pack()        

        self.labelNomeCurso = tk.Label(self.frameNomeCurso, text="Informe o nome do curso: ")
        self.labelNomeCurso.pack(side="left")
        self.inputNomeCurso = tk.Entry(self.frameNomeCurso, width=20)
        self.inputNomeCurso.pack(side="right")

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