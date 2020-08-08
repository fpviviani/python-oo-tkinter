import tkinter as tk
from models import Grade as gr
from views.grades import LimiteInsereGrade as lig
from views.grades import LimiteMostraGrades as lmg
from views.grades import LimiteConsultaGrade as lcg
import os.path
import pickle

class CtrlGrade():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisciplinasGrade = []
        if not os.path.isfile("grade.pickle"):
            self.listaGrades =  []
        else:
            with open("grade.pickle", "rb") as f:
                self.listaGrades = pickle.load(f)
        
    def salvar(self):
        if len(self.listaGrades) != 0:
            with open("grades.pickle","wb") as f:
                pickle.dump(self.listaGrades, f)

    # Método que chama a view para inserir uma disciplina
    def insereGrade(self):
        self.listaDisciplinasGrade = []
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = lig.LimiteInsereGrade(self, listaDisciplinas, listaCursos) 

    # Método que chama a view para consultar uma grade
    def consultaGrade(self):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        self.limiteIns = lcg.LimiteConsultaGrade(self, listaCursos) 

    # Método que chama a view que irá exibir uma grade específica
    def gradeConsultada(self, event):
        nomeCurso = self.limiteIns.escolhaCombo.get()
        curso = self.ctrlPrincipal.ctrlCurso.getCurso(nomeCurso)
        grade = curso.getGrade()
    
        str = ''
        str += 'Ano: ' + grade.getAno() + '\n'
        str += 'Disciplinas: \n'
        for disciplina in grade.getDisciplinas():
            str += '    ' + disciplina.getCodigo() + '\n'
        str += 'Curso: ' + grade.getCurso().getNome() + '\n'
        str += '------\n'

        self.limiteLista = lmg.LimiteMostraGrades(str)
        self.limiteIns.lift()

    # Método que chama a view que irá exibir uma lista com todas as grades
    def mostraGrades(self):
        str = ''
        for grade in self.listaGrades:
            str += 'Ano: ' + grade.getAno() + '\n'
            str += 'Disciplinas: \n'
            for disciplina in grade.getDisciplinas():
                str += '    ' + disciplina.getCodigo() + '\n'
            str += 'Curso: ' + grade.getCurso().getNome() + '\n'
            str += '------\n'

        self.limiteLista = lmg.LimiteMostraGrades(str)

    # Método que realizará o cadastro da grade
    def criaGrade(self, event):
        ano = self.limiteIns.inputAno.get()
        nomeCurso = self.limiteIns.escolhaCombo.get()
        curso = self.ctrlPrincipal.ctrlCurso.getCurso(nomeCurso)
        # Valida se todos os campos foram preenchidos
        if (ano == "" or nomeCurso == None):
            self.limiteIns.mostraJanela('Erro', 'Todos os campos precisam ser preenchidos')
            self.limiteIns.lift()
            return
        grade = gr.Grade(ano, self.listaDisciplinasGrade, curso)
        curso.setGrade(grade)
        self.listaGrades.append(grade)
        self.limiteIns.mostraJanela('Sucesso', 'Grade criada com sucesso')
        self.limiteIns.lift()
        self.limiteIns.destroy()
        
    # Método que chama a view para a inserção de disciplinas na grade
    def insereDisciplina(self, event):
        discSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        self.listaDisciplinasGrade.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina inserida')
        self.limiteIns.lift()
        self.limiteIns.listbox.delete(tk.ACTIVE)
    