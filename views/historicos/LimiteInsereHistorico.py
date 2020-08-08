import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereHistorico(tk.Toplevel):
    def __init__(self, controle, listaAlunos):

        tk.Toplevel.__init__(self)
        self.geometry('300x80')
        self.title("Grade")
        self.controle = controle

        self.frameAluno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAluno.pack()
        self.frameButton.pack()        

        self.labelAluno = tk.Label(self.frameAluno,text="Escolha o aluno: ")
        self.labelAluno.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameAluno, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaAlunos

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Histórico")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaHistorico)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)   