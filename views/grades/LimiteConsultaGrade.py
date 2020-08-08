import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteConsultaGrade(tk.Toplevel):

    def __init__(self, controle, listaCursos):

        tk.Toplevel.__init__(self)
        self.geometry('250x80')
        self.title("Consulta")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro, text="Curso: ")
        self.labelNro.pack(side="left")

        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNro, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button-1>", lambda event: controle.gradeConsultada(event))

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)