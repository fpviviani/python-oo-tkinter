from models import Curso as cur
from views.cursos import LimiteInsereCurso as lic
from views.cursos import LimiteConsultaCurso as lcc
from views.cursos import LimiteMostraCursos as lmc
import os.path
import pickle

class CtrlCurso():       
    def __init__(self):
        if not os.path.isfile("curso.pickle"):
            self.listaCursos =  []
        else:
            with open("curso.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)
            
    def salvar(self):
        if len(self.listaCursos) != 0:
            with open("curso.pickle","wb") as f:
                pickle.dump(self.listaCursos, f)

    # Método que retorna uma lista com os cursos
    def getListaCursos(self):
        return self.listaCursos

    # Método que busca por um curso específico
    def getCurso(self, nome):
        cursoRet = None
        for curso in self.listaCursos:
            if (curso.getNome() == nome):
                cursoRet = curso
        return cursoRet

    # Método que retorna uma lista com os nomes dos cursos
    def getListaNomeCursos(self):
        listaNome = []
        for curso in self.listaCursos:
            listaNome.append(curso.getNome())
        return listaNome

    # Método que chama a view para inserir novos cursos
    def insereCursos(self):
        self.limiteIns = lic.LimiteInsereCurso(self) 

    # Método que chama a view para consultar um curso
    def consultaCurso(self):
        self.limiteIns = lcc.LimiteConsultaCurso(self) 

    # Método que chama a view que exibirá uma lista com todos os cursos
    def mostraCursos(self):
        string = 'Nome -- Grade\n'
        for curso in self.listaCursos:
            if (curso.getGrade() == None):
                grade = "Curso ainda não tem grade."
            else:
                grade = str(curso.getGrade().getAno())
            string += curso.getNome() + ' -- ' + grade + '\n'
        self.limiteLista = lmc.LimiteMostraCursos(string)

    # Método que vai realizar a consulta ou a inserção de um curso
    def enterHandler(self, event, type):
        if (type == "consulta"):
            nomeCurso = self.limiteIns.inputNomeCurso.get()
            curso = self.getCurso(nomeCurso)
            if (curso == None):
                self.limiteIns.mostraJanela('Falha', "Não foi encontrado nenhum curso com o nome informado.")
            else:
                dadosCurso = 'Nome: ' + curso.getNome() + '\n'
                if (curso.getGrade() == None):
                    grade = "Curso ainda não tem grade."
                else:
                    grade = str(curso.getGrade().getAno())
                dadosCurso += 'Grade: ' + grade + '\n'
                self.limiteIns.mostraJanela('Sucesso', dadosCurso)
            
            # Eleva a janela de inserção/consulta pra cima da main window
            self.limiteIns.lift()
            self.clearHandler(event, type)

        elif (type == "insere"):
            nomeCurso = self.limiteIns.inputNomeCurso.get()
            # Valida se existe outro curso com aquele nome
            for curso in self.listaCursos:
                if (curso.getNome() == nomeCurso):
                    self.limiteIns.mostraJanela('Erro', 'Já existe um curso com esse nome')
                    self.limiteIns.lift()
                    return
            # Valida se todos os campos foram preenchidos
            if (nomeCurso == ""):
                self.limiteIns.mostraJanela('Erro', 'Todos os campos precisam ser preenchidos')
                self.limiteIns.lift()
                return
            curso = cur.Curso(nomeCurso)
            self.listaCursos.append(curso)
            self.limiteIns.mostraJanela('Sucesso', 'Curso cadastrado com sucesso')
            # Eleva a janela de inserção/consulta pra cima da main window
            self.limiteIns.lift()
            self.clearHandler(event, type)

    # Limpa os campos da janela de inserção/consulta
    def clearHandler(self, event, type):
        self.limiteIns.inputNomeCurso.delete(0, len(self.limiteIns.inputNomeCurso.get()))

    # Destrói a janela de inserção/consulta
    def fechaHandler(self, event, type):
        self.limiteIns.destroy()
    