import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereDisciplinaHistorico(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaAlunos):

        tk.Toplevel.__init__(self)
        self.geometry('600x200')
        self.title("Histórico")
        self.controle = controle

        self.frameAluno = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSem = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAluno.pack()
        self.frameDiscip.pack()
        self.frameAno.pack()
        self.frameSem.pack()
        self.frameNota.pack()
        self.frameButton.pack()        

        self.labelAluno = tk.Label(self.frameAluno,text="Informe o aluno do qual se deseja inserir disciplinas no histórico: ")
        self.labelAluno.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameAluno, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaAlunos

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox2.pack(side="left")
        self.combobox2['values'] = listaCodDiscip

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelSem = tk.Label(self.frameSem,text="Semestre: ")
        self.labelAno.pack(side="left")
        self.labelSem.pack(side="left")

        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")
        self.inputSem = tk.Entry(self.frameSem, width=20)
        self.inputSem.pack(side="left")

        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelNota.pack(side="left")

        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Disciplina")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.cadastraDisciplinaHistorico)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)   