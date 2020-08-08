import tkinter as tk
from models import Historico as hist
from views.historicos import LimiteInsereHistorico as lih
from views.historicos import LimiteInsereDisciplinaHistorico as lid
from views.historicos import LimiteConsultaHistorico as lch
from views.historicos import LimiteMostraHistoricos as lmh
import os.path
import pickle

class CtrlHistorico():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisciplinasHistoricos = []
        if not os.path.isfile("historico.pickle"):
            self.listaHistoricos =  []
        else:
            with open("historico.pickle", "rb") as f:
                self.listaHistoricos = pickle.load(f)
        if not os.path.isfile("alunos-historico.pickle"):
            self.listaAlunosHistoricos =  []
        else:
            with open("alunos-historico.pickle", "rb") as f:
                self.listaAlunosHistoricos = pickle.load(f)

    def salvar(self):
        if len(self.listaHistoricos) != 0:
            with open("historico.pickle","wb") as f:
                pickle.dump(self.listaHistoricos, f)

        if len(self.listaAlunosHistoricos) != 0:
            with open("alunos-historico.pickle","wb") as f:
                pickle.dump(self.listaAlunosHistoricos, f)

    # Método que chama a view para inserir um histórico
    def insereHistorico(self):
        listaAlunos = self.ctrlPrincipal.ctrlAluno.getListaNroMatricula()

        for nro in listaAlunos:
            # Confere os alunos que já possuem histórico cadastrado 
            # e os remove da lista de alunos que será enviada para a view
            if (nro in self.listaAlunosHistoricos):
                listaAlunos.remove(nro)

        self.limiteIns = lih.LimiteInsereHistorico(self, listaAlunos) 

    # Método que chama a view para consulta um histórico
    def consultaHistorico(self):
        listaAlunos = self.ctrlPrincipal.ctrlAluno.getListaNroMatricula()
        for nro in listaAlunos:
            # Confere os alunos que já possuem histórico cadastrado 
            # e os remove da lista de alunos que será enviada para a view
            if (nro not in self.listaAlunosHistoricos):
                listaAlunos.remove(nro)
        self.limiteIns = lch.LimiteConsultaHistorico(self, listaAlunos) 

    # Método que chama a view que irá exibir um histórico específico
    def historicoConsultado(self, event):
        cargaEletiva = 0
        cargaObrigatoria = 0
        nroMatricula = self.limiteIns.escolhaCombo.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(nroMatricula)
        historico = aluno.getHistorico()
        if (historico == None):
            self.limiteIns.mostraJanela('Falha', "Aluno ainda não tem histórico cadastrado.")
        else:
            dadosHist = aluno.getNome() + ' -- ' + aluno.getNroMatric() + '\n'
            dadosHist += 'Curso: ' + aluno.getCurso().getNome() + '\n'
            dadosHist += 'Disciplinas:\n'
            dadosHist += '    Cod - Data cursada - Nota - Status\n\n    '
            
            # Agrupa as disciplinas pela data cursada
            datas = dict()
            for disciplina in historico.getDisciplinas():
                dataDisc = int(disciplina['Ano'] + disciplina['Semestre'])
                if (dataDisc not in datas):
                    datas[dataDisc] = []
                    datas[dataDisc].append(disciplina)
                else:
                    datas[dataDisc].append(disciplina)
            
            for datasDisc in sorted(datas):

                for disciplina in datas[datasDisc]:
                    dadosHist += disciplina['Codigo'] + ' - ' + disciplina['Ano'] + '.' + disciplina['Semestre'] + ' - '              
                    if (float(disciplina['Nota'].replace(',', '.')) >= 6):
                        if (float(disciplina['Nota'].replace(',', '.')) > 10):
                            nota = float(disciplina['Nota'].replace(',', '.'))/10
                            if (nota >= 6):
                                status = "Aprovado"
                            else:
                                status = "Reprovado"
                        else:
                            nota = float(disciplina['Nota'].replace(',', '.'))
                            status = "Aprovado"
                    else:
                        nota = float(disciplina['Nota'].replace(',', '.'))
                        status = "Reprovado"

                    dadosHist += disciplina['Nota'] + ' - ' + status + '\n'
                    dadosHist += '------\n'

                    disciplinaObj = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplina['Codigo'])
                    # Confere se a disciplina é obrigatória e soma a carga horária
                    if (disciplinaObj in aluno.getCurso().getGrade().getDisciplinas()):
                        cargaObrigatoria = cargaObrigatoria + int(disciplinaObj.getCargaHoraria())
                    else:
                        cargaEletiva = cargaEletiva + int(disciplinaObj.getCargaHoraria())

            dadosHist += 'Carga horária cursada em disciplinas obrigatórias: ' + str(cargaObrigatoria) + '\n'
            dadosHist += 'Carga horária cursada em disciplinas eletivas: ' + str(cargaEletiva) + '\n'
            self.limiteIns.mostraJanela('Sucesso', dadosHist)
        
        self.limiteIns.lift()

    # Método que irá cadastrar o histórico
    def criaHistorico(self, event):
        nroMatricula = self.limiteIns.escolhaCombo.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(nroMatricula)
        historico = hist.Historico(aluno)
        aluno.setHistorico(historico)
        self.listaHistoricos.append(historico)
        self.listaAlunosHistoricos.append(aluno.getNroMatric())
        self.limiteIns.mostraJanela('Sucesso', 'Histórico criado com sucesso')
        self.limiteIns.lift()
        self.limiteIns.destroy()
        
    # Método que chama a view para inserir disciplinas no histórico
    def insereDisciplina(self):
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = lid.LimiteInsereDisciplinaHistorico(self, listaDisciplinas, self.listaAlunosHistoricos)

    # Método que cadastra disciplinas no histórico
    def cadastraDisciplinaHistorico(self, event):
        alunoNroMatric = self.limiteIns.escolhaCombo.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoNroMatric)
        historico = aluno.getHistorico()
        discCod = self.limiteIns.escolhaCombo2.get()
        try:
            ano = int(self.limiteIns.inputAno.get())
            semestre = int(self.limiteIns.inputSem.get())
        except ValueError:
            self.limiteIns.mostraJanela('Erro', 'Os campos ano e semestre devem conter apenas números')
            self.limiteIns.lift()
            return
        nota = self.limiteIns.inputNota.get()
        # Valida se todos os campos foram preenchidos
        if (ano == "" or semestre == "" or nota == "" or discCod == None):
            self.limiteIns.mostraJanela('Erro', 'Todos os campos precisam ser preenchidos')
            self.limiteIns.lift()
            return
        disciplina = {
            "Disciplina": self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discCod),
            "Codigo": str(discCod),
            "Ano": str(ano),
            "Semestre": str(semestre),
            "Nota": nota
        }
        historico.addDisciplina(disciplina)
        self.listaDisciplinasHistoricos.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina inserida')
        self.limiteIns.destroy()

    # Método que chama a view que irá exibir todos os históricos
    def mostraHistoricos(self):

        for historico in self.listaHistoricos:
            cargaEletiva = 0
            cargaObrigatoria = 0
            aluno = historico.getAluno()
            dadosHist = aluno.getNome() + ' -- ' + aluno.getNroMatric() + '\n'
            dadosHist += 'Curso: ' + aluno.getCurso().getNome() + '\n'
            dadosHist += 'Disciplinas:\n'
            dadosHist += '    Cod - Data cursada - Nota - Status\n\n    '
            
            # Agrupa as disciplinas pela data cursada
            datas = dict()
            for disciplina in historico.getDisciplinas():
                dataDisc = int(disciplina['Ano'] + disciplina['Semestre'])
                if (dataDisc not in datas):
                    datas[dataDisc] = []
                    datas[dataDisc].append(disciplina)
                else:
                    datas[dataDisc].append(disciplina)
            
            for datasDisc in sorted(datas):

                for disciplina in datas[datasDisc]:
                    dadosHist += disciplina['Codigo'] + ' - ' + disciplina['Ano'] + '.' + disciplina['Semestre'] + ' - '              
                    if (float(disciplina['Nota'].replace(',', '.')) >= 6):
                        if (float(disciplina['Nota'].replace(',', '.')) > 10):
                            nota = float(disciplina['Nota'].replace(',', '.'))/10
                            if (nota >= 6):
                                status = "Aprovado"
                            else:
                                status = "Reprovado"
                        else:
                            nota = float(disciplina['Nota'].replace(',', '.'))
                            status = "Aprovado"
                    else:
                        nota = float(disciplina['Nota'].replace(',', '.'))
                        status = "Reprovado"

                    dadosHist += disciplina['Nota'] + ' - ' + status + '\n'
                    dadosHist += '------\n'

                    disciplinaObj = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplina['Codigo'])
                    # Confere se a disciplina é obrigatória e soma a carga horária
                    if (disciplinaObj in aluno.getCurso().getGrade().getDisciplinas()):
                        cargaObrigatoria = cargaObrigatoria + int(disciplinaObj.getCargaHoraria())
                    else:
                        cargaEletiva = cargaEletiva + int(disciplinaObj.getCargaHoraria())

            dadosHist += 'Carga horária cursada em disciplinas obrigatórias: ' + str(cargaObrigatoria) + '\n'
            dadosHist += 'Carga horária cursada em disciplinas eletivas: ' + str(cargaEletiva) + '\n'
            dadosHist += '------\n'
        self.limiteLista = lmh.LimiteMostraHistoricos(dadosHist)
            