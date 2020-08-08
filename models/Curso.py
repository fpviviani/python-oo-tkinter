from models import Grade as g

class Curso():

    def __init__(self, nome):
        self.__nome = nome
        self.__grade = None

    def getNome(self):
        return self.__nome

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        self.__grade = grade
