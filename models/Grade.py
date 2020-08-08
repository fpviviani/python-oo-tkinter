class Grade():

    def __init__(self, ano, disciplinas, curso):
        self.__ano = ano
        self.__disciplinas = disciplinas
        self.__curso = curso

    def getAno(self):
        return self.__ano

    def getDisciplinas(self):
        return self.__disciplinas

    def getCurso(self):
        return self.__curso

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)