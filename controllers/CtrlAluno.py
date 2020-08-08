from models import Aluno as alu
from views.alunos import LimiteInsereAluno as lia
from views.alunos import LimiteMostraAlunos as lma
from views.alunos import LimiteConsultaAluno as lca
import os.path
import pickle

class CtrlAluno():       
    def __init__(self, controlePrincipal):
        if not os.path.isfile("aluno.pickle"):
            self.listaAlunos =  []
        else:
            with open("aluno.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)
        self.ctrlPrincipal = controlePrincipal

    def salvar(self):
        if len(self.listaAlunos) != 0:
            with open("aluno.pickle","wb") as f:
                pickle.dump(self.listaAlunos, f)

    # Método que chama a view para inserir novos alunos
    def insereAlunos(self):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        self.limiteInsere = lia.LimiteInsereAluno(self, listaCursos) 

    # Método que chama a view para consultar um aluno
    def consultaAluno(self):
        self.limiteInsere = lca.LimiteConsultaAluno(self) 

    # Método que busca por um aluno específico
    def getAluno(self, nroMatric):
        alunoRet = None
        for aluno in self.listaAlunos:
            if (aluno.getNroMatric() == nroMatric):
                alunoRet = aluno
        
        return alunoRet

    # Método que retorna uma lista com os nomes dos alunos
    def getListaNomeAlunos(self):
        listaNome = []
        for aluno in self.listaAlunos:
            listaNome.append(aluno.getNome())
        return listaNome

    # Método que retorna uma lista com os números de matricula dos alunos
    def getListaNroMatricula(self):
        listaNome = []
        for aluno in self.listaAlunos:
            listaNome.append(aluno.getNroMatric())
        return listaNome

    # Método que chama a view que vai exibir uma lista com todos os alunos e seus dados
    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome -- Curso\n'
        for aluno in self.listaAlunos:
            str += aluno.getNroMatric() + ' -- ' + aluno.getNome() + ' -- ' + aluno.getCurso() + '\n'     
              
        self.limiteLista = lma.LimiteMostraAlunos(str)

    # Método que vai realizar a consulta ou a inserção de um aluno
    def enterHandler(self, event, type):
        if (type == "consulta"):
            nroMatric = self.limiteInsere.inputNro.get()
            aluno = self.getAluno(nroMatric)
            if (aluno == None):
                self.limiteInsere.mostraJanela('Falha', "Não foi encontrado nenhum aluno com o número de matricula informado.")
            else:
                dadosAluno = aluno.getNome() + ' -- ' + aluno.getNroMatric() + ' -- ' + aluno.getCurso().getNome()
                self.limiteInsere.mostraJanela('Sucesso', dadosAluno)
            self.clearHandler(event, type)

        elif (type == "insere"):
            nroMatric = self.limiteInsere.inputNro.get()
            # Valida se existe outro aluno com aquele número antes de inserir
            for aluno in self.listaAlunos:
                if (aluno.getNroMatric() == nroMatric):
                    self.limiteInsere.mostraJanela('Erro', 'Já existe um aluno com esse número')
                    self.limiteInsere.lift()
                    return
            nome = self.limiteInsere.inputNome.get()
            cursoNome = self.limiteInsere.escolhaCombo.get()
            curso = self.ctrlPrincipal.ctrlCurso.getCurso(cursoNome)
            # Valida se todos os campos foram preenchidos
            if (nroMatric == "" or nome == "" or curso == None):
                    self.limiteInsere.mostraJanela('Erro', 'Todos os campos precisam ser preenchidos')
                    self.limiteInsere.lift()
                    return
            aluno = alu.Aluno(nroMatric, nome, curso)
            self.listaAlunos.append(aluno)
            self.limiteInsere.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
            self.clearHandler(event, type)
        
        # Eleva a janela de inserção/consulta pra cima da main window
        self.limiteInsere.lift()

    # Limpa os campos da janela de inserção/consulta
    def clearHandler(self, event, type):
        self.limiteInsere.inputNro.delete(0, len(self.limiteInsere.inputNro.get()))
        if (type == "insere"):
            self.limiteInsere.inputNome.delete(0, len(self.limiteInsere.inputNome.get()))
            self.limiteInsere.escolhaCombo.set('')

    # Destrói a janela de inserção/consulta
    def fechaHandler(self, event, type):
        self.limiteInsere.destroy()
    