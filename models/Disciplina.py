class Disciplina():

    def __init__(self, cod, nome, cargaHoraria):
        self.__cod = cod
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__cod

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria
