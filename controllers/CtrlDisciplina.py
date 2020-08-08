from models import Disciplina as disc
from views.disciplinas import LimiteInsereDisciplinas as lid
from views.disciplinas import LimiteConsultaDisciplina as lcd
from views.disciplinas import LimiteMostraDisciplinas as lmd
import os.path
import pickle

class CtrlDisciplina():       
    def __init__(self):
        if not os.path.isfile("disciplina.pickle"):
            self.listaDisciplinas =  []
        else:
            with open("disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)
            
    def salvar(self):
        if len(self.listaDisciplinas) != 0:
            with open("disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    # Método que retorna uma lista com as disciplinas
    def getListaDisciplinas(self):
        return self.listaDisciplinas

    # Método que busca uma disciplina específica
    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if (disc.getCodigo() == codDisc):
                discRet = disc
        return discRet

    # Método que retorna uma lista com os códigos das disciplinas
    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    # Método que chama a view para inserir uma nova disciplina
    def insereDisciplinas(self):
        self.limiteIns = lid.LimiteInsereDisciplinas(self) 

    # Método que chama a view para consultar uma disciplina
    def consultaDisciplinas(self):
        self.limiteIns = lcd.LimiteConsultaDisciplina(self) 

    # Método que chama a view que irá exibir uma lista com todas as disciplinas
    def mostraDisciplinas(self):
        string = 'Código -- Nome -- Carga Horária\n'
        for disc in self.listaDisciplinas:
            string += disc.getCodigo() + ' -- ' + disc.getNome() + ' -- ' + str(disc.getCargaHoraria()) + 'h' + '\n'
        self.limiteLista = lmd.LimiteMostraDisciplinas(string)

    # Método que vai realizar a consulta ou a inserção de uma disciplina
    def enterHandler(self, event, type):
        if (type == "consulta"):
            codDisc = self.limiteIns.inputCodigo.get()
            disciplina = self.getDisciplina(codDisc)
            if (disciplina == None):
                self.limiteIns.mostraJanela('Falha', "Não foi encontrada nenhuma disciplina com o código informado.")
            else:
                dadosDisc = disciplina.getNome() + ' -- ' + disciplina.getCodigo() + ' -- ' + str(disciplina.getCargaHoraria()) + 'h'
                self.limiteIns.mostraJanela('Sucesso', dadosDisc)
            self.clearHandler(event, type)

        elif (type == "insere"):
            codDisc = self.limiteIns.inputCodigo.get()
            # Valida se existe outra disciplina com aquele código
            for disci in self.listaDisciplinas:
                if (disci.getCodigo() == codDisc):
                    self.limiteIns.mostraJanela('Erro', 'Já existe uma disciplina com esse código')
                    self.limiteIns.lift()
                    return
            nome = self.limiteIns.inputNome.get()
            cargaHoraria = self.limiteIns.inputCargaHoraria.get()
            # Valida se a carga horária digitada é um número
            try:
                cargaHoraria = int(cargaHoraria)
            except ValueError:
                self.limiteIns.mostraJanela('Erro', 'A carga horaria deve conter apenas números')
                self.limiteIns.lift()
                return
            
            # Valida se todos os campos foram preenchidos
            if (codDisc == "" or nome == "" or cargaHoraria == ""):
                self.limiteIns.mostraJanela('Erro', 'Todos os campos precisam ser preenchidos')
                self.limiteIns.lift()
                return

            disciplina = disc.Disciplina(codDisc, nome, cargaHoraria)
            self.listaDisciplinas.append(disciplina)
            self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
            self.clearHandler(event, type)
        
        # Eleva a janela de inserção/consulta pra cima da main window
        self.limiteIns.lift()

    # Limpa os campos da janela de inserção/consulta
    def clearHandler(self, event, type):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        if (type == "insere"):
            self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
            self.limiteIns.inputCargaHoraria.delete(0, len(self.limiteIns.inputCargaHoraria.get()))

    # Destrói a janela de inserção/consulta
    def fechaHandler(self, event, type):
        self.limiteIns.destroy()
    