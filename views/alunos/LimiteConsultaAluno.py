import tkinter as tk
from tkinter import messagebox

class LimiteConsultaAluno(tk.Toplevel):

    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x80')
        self.title("Consulta")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro, text="Nro Matrícula: ")
        self.labelNro.pack(side="left")

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="right")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        type = "consulta"
        self.buttonSubmit.bind("<Button-1>", lambda event, arg=type: controle.enterHandler(event, type))

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button-1>", lambda event, arg=type: controle.clearHandler(event, type))

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button-1>", lambda event, arg=type: controle.fechaHandler(event, type))

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)