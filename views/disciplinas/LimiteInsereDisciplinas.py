import tkinter as tk
from tkinter import messagebox

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameCargaHoraria = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHoraria.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCargaHoraria = tk.Label(self.frameCargaHoraria, text="Carga Horaria: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")  
        self.labelCargaHoraria.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")       
        self.inputCargaHoraria = tk.Entry(self.frameCargaHoraria, width=20)
        self.inputCargaHoraria.pack(side="left")           
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        type = "insere"
        self.buttonSubmit.bind("<Button>", lambda event, arg=type: controle.enterHandler(event, type))
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", lambda event, arg=type: controle.clearHandler(event, type))  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", lambda event, arg=type: controle.fechaHandler(event, type))

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        