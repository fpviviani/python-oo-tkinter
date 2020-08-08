import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from models import Aluno as alu
from controllers import CtrlDisciplina as cd
from controllers import CtrlGrade as cg
from controllers import CtrlAluno as ca
from controllers import CtrlCurso as cc
from controllers import CtrlHistorico as ch

class LimitePrincipal():

    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('400x300')
        self.menubar = tk.Menu(self.root, bg='#366998')
        self.cursoMenu = tk.Menu(self.menubar, bg='#E66C63')
        self.alunoMenu = tk.Menu(self.menubar, bg='#E66C63')
        self.discipMenu = tk.Menu(self.menubar, bg='#E66C63')
        self.gradeMenu = tk.Menu(self.menubar, bg='#E66C63')
        self.histMenu = tk.Menu(self.menubar, bg='#E66C63')
        self.sairMenu = tk.Menu(self.menubar, bg='#E66C63')

        self.discipMenu.add_command(label="Insere", command=lambda: self.controle.insereDisciplinas())
        self.discipMenu.add_command(label="Mostra", command=lambda: self.controle.mostraDisciplinas())
        self.discipMenu.add_command(label="Consulta", command=lambda: self.controle.consultaDisciplina())
        self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)
        self.cursoMenu.add_command(label="Insere", command=lambda: self.controle.insereCursos())
        self.cursoMenu.add_command(label="Mostra", command=lambda: self.controle.mostraCursos())
        self.cursoMenu.add_command(label="Consulta", command=lambda: self.controle.consultaCurso())
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)
        self.gradeMenu.add_command(label="Insere", command=lambda: self.controle.insereGrade())
        self.gradeMenu.add_command(label="Mostra", command=lambda: self.controle.mostraGrades())
        self.gradeMenu.add_command(label="Consulta", command=lambda: self.controle.consultaGrade())
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)
        self.alunoMenu.add_command(label="Insere", command=lambda: self.controle.insereAlunos())
        self.alunoMenu.add_command(label="Mostra", command=lambda: self.controle.mostraAlunos())
        self.alunoMenu.add_command(label="Consulta", command=lambda: self.controle.consultaAluno())
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)
        self.histMenu.add_command(label="Insere", command=lambda: self.controle.insereHistorico())
        self.histMenu.add_command(label="Insere Disciplina no Histórico", command=lambda: self.controle.insereDisciplinaHistorico())
        self.histMenu.add_command(label="Mostra", command=lambda: self.controle.mostraHistoricos())
        self.histMenu.add_command(label="Consulta", command=lambda: self.controle.consultaHistorico())
        self.menubar.add_cascade(label="Histórico", menu=self.histMenu)
        self.sairMenu.add_command(label="Salvar", command=lambda: self.controle.salvar())
        self.menubar.add_cascade(label="Salvar", menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        # Adiciona imagem de fundo para o programa
        self.canvas = tk.Canvas(self.root, width=300, height=400)
        self.image = ImageTk.PhotoImage(Image.open("assets/images/bg-unifei.png"))
        self.canvas.create_image(0, 0, anchor=tk.NW, image = self.image)
        self.canvas.pack()

        # Instancia as controllers que serão usadas
        self.ctrlCurso = cc.CtrlCurso()
        self.ctrlAluno = ca.CtrlAluno(self)
        self.ctrlDisciplina = cd.CtrlDisciplina()
        self.ctrlGrade = cg.CtrlGrade(self)
        self.ctrlHistorico = ch.CtrlHistorico(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho Final - COM220")

        # Inicia o mainloop
        self.root.mainloop()
       
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos()

    def consultaAluno(self):
        self.ctrlAluno.consultaAluno()

    def mostraAlunos(self):
        self.ctrlAluno.mostraAlunos()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def consultaDisciplina(self):
        self.ctrlDisciplina.consultaDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def insereCursos(self):
        self.ctrlCurso.insereCursos()

    def consultaCurso(self):
        self.ctrlCurso.consultaCurso()

    def mostraCursos(self):
        self.ctrlCurso.mostraCursos()

    def insereGrade(self):
        self.ctrlGrade.insereGrade()

    def mostraGrades(self):
        self.ctrlGrade.mostraGrades()
    
    def consultaGrade(self):
        self.ctrlGrade.consultaGrade()

    def insereHistorico(self):
        self.ctrlHistorico.insereHistorico()

    def insereDisciplinaHistorico(self):
        self.ctrlHistorico.insereDisciplina()

    def mostraHistoricos(self):
        self.ctrlHistorico.mostraHistoricos()
        
    def consultaHistorico(self):
        self.ctrlHistorico.consultaHistorico()

    def salvar(self):
        self.ctrlAluno.salvar()
        self.ctrlCurso.salvar()
        self.ctrlDisciplina.salvar()
        self.ctrlGrade.salvar()
        self.ctrlHistorico.salvar()


if __name__ == '__main__':
    c = ControlePrincipal()