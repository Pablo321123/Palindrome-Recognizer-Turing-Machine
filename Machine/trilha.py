from abstractFita import *


class Trilha(AbstractFita):
    def __init__(self, palavra: str, numTrilha: int, charInicio, charBranco) -> None:
        self.palavra = palavra
        self.numTrilha = numTrilha
        self.charInicio = charInicio
        self.charBranco = charBranco
        self.cabecote = 1  # Controlador da posiçao a ser lida na trilha
        self.fita = []
        self.tamFita = 0  # controla o tamanho da fita
        self.montarFita()

    def montarFita(self):
        self.fita = [[self.charBranco] *
                     len(self.palavra) for _ in range(self.numTrilha)]
        self.fita[0] = list(self.charInicio + self.palavra)
        self.fita[1].append(self.charBranco)
        self.tamFita = len(self.fita[0])
        self.adicionarBlocosDireita()
        self.adicionarBlocosDireita()

    # como a ideia é ter uma fita com trilhas infinitas a direita, sempre que requisitadas será adicionados os blocos a direita, a fim de economizar memoria
    def adicionarBlocosDireita(self):
        for i in range(self.numTrilha):
            self.fita[i].append(self.charBranco)
        self.tamFita += 1

    # Substitui os simbolos na fita
    def subSimbolosFita(self, lst_charSubs):
        for i in range(self.numTrilha):
            self.fita[i][self.cabecote] = lst_charSubs[i]

    # move o cabeçote para Direita
    def moverDireita(self, lst_charSubs):
        self.subSimbolosFita(lst_charSubs)
        self.cabecote += 1

        # Caso o cabeçote alcance o tamanho da fita, significa que precisamos criar mais blocos a direita, uma vez que a fita é inifinita
        if self.cabecote == self.tamFita:
            self.adicionarBlocosDireita()
        # print('Cabeçote andou para direita')

    # move o cabeçote para Esquerda
    def moverEsquerda(self, lst_charSubs):
        self.subSimbolosFita(lst_charSubs)
        self.cabecote -= 1

        if self.cabecote == self.tamFita:
            self.adicionarBlocosDireita()
        # print('Cabeçote andou para esquerda')

    # Retorna os simbolos antuais na fita
    def getEstadoAtual(self):
        return [self.fita[0][self.cabecote], self.fita[1][self.cabecote]]
