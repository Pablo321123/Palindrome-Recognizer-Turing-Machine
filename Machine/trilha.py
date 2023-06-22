from abstractFita import *


class Trilha(AbstractFita):
    def __init__(self, palavra: str, numTrilha: int, charInicio, charBranco) -> None:
        self.palavra = palavra
        self.numTrilha = numTrilha
        self.charInicio = charInicio
        self.charBranco = charBranco
        self.cabecote = 1  # Controlador da posiçao a ser lida na trilha
        self.fita = []
        self.montarFita()

    def montarFita(self):
        self.fita = [[self.charBranco] *
                     len(self.palavra) for _ in range(self.numTrilha)]
        self.fita[0] = list(self.charInicio + self.palavra)
        self.adicionarBlocosDireita()

    def adicionarBlocosDireita(self):  # como a ideia é ter uma fita com trilhas infinitas a direita, sempre que requisitadas será adicionados os blocos a direita, a fim de economizar memoria
        for i in range(self.numTrilha):
            self.fita[i].append(self.charBranco)
        print(self.fita)
        
    def subSimbolosFita(self, lst_charSubs):
        for i in range(self.numTrilha):
            self.fita[i][self.cabecote] = lst_charSubs[i]

    def moverDireita(self, lst_charSubs):
        self.subSimbolosFita(lst_charSubs)            
        self.cabecote += 1
        print('Cabeçote andou para direita')

    def moverEsquerda(self, lst_charSubs):
        self.subSimbolosFita(lst_charSubs)            
        self.cabecote -= 1
        print('Cabeçote andou para esquerda')

    def getEstadoAtual(self):
        return self.fita[self.cabecote]
