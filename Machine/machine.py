from trilha import *


class MaquinaTuring:
    def __init__(self, numTrilhas: int, estados, alfabetoMaquina, alfabetoFita, charInicio, charBranco, trasicoes, estadoIncial, estadosFinais, palavra):
        self.numTrilhas = numTrilhas
        self.estados = estados
        self.alfabetoMaquina = alfabetoMaquina
        self.alfabetoFita = alfabetoFita
        self.charInicio = charInicio
        self.charBranco = charBranco
        self.trasicoes = trasicoes
        self.estadoIncial = estadoIncial
        self.estadosFinais = estadosFinais
        self.maquina = Trilha(palavra)
