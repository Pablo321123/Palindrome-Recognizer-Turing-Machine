from collections import OrderedDict
from trilha import *
from funcaoTransicao import *


class MaquinaTuring:
    def __init__(self, numTrilhas: int, estados, alfabetoMaquina, alfabetoFita, charInicio, charBranco, trasicoes, estadoIncial, estadosFinais, palavra: str):
        self.numTrilhas = numTrilhas
        self.estados = estados
        self.alfabetoMaquina = alfabetoMaquina
        self.alfabetoFita = alfabetoFita
        self.charInicio = charInicio
        self.charBranco = charBranco
        self.trasicoes: OrderedDict[str, FuncaoTransicao] = self.definirTransicoes(
            trasicoes)
        self.estadoIncial = estadoIncial
        self.estadosFinais = estadosFinais
        self.estadoAtual = self.estadoIncial
        self.palavra = palavra
        self.maquina = Trilha(palavra, self.numTrilhas,
                              self.charInicio, self.charBranco)

    def iniciarMaquina(self) -> bool:
        while True:                       
            if  not self.moverCabecote(self.lerCabecote()):
                return self.responder()

    def responder(self) -> bool:
        if self.estadoAtual in self.estadosFinais:
            return True
        return False

    def definirTransicoes(self, lstTransicoes) -> OrderedDict():
        dicTransic = OrderedDict()
        for a in lstTransicoes:
            # Pega na lista o proximo estado (a[1:]) pega todos os elementos a partir da segunda posição
            proxEstado = self.numTrilhas+1
            # Caso não exista um caminho para a trasincao, cria, caso contrario adiciona
            if a[0] in dicTransic:
                dicTransic[a[0]].append(FuncaoTransicao(
                    a[0], a[proxEstado], a[1:self.numTrilhas + 1], a[proxEstado + 1:-1], a[-1]))
            else:
                dicTransic[a[0]] = [FuncaoTransicao(
                    a[0], a[proxEstado], a[1:self.numTrilhas + 1], a[proxEstado + 1:-1], a[-1])]

        return dicTransic

    def lerCabecote(self) -> list:
        return self.maquina.getEstadoAtual()

    def moverCabecote(self, lst_simbs) -> bool:
        noPath = False
                
        for t in self.trasicoes[self.estadoAtual]:
            t: FuncaoTransicao
            if t.lst_simbsE == lst_simbs:                
                noPath = True
                                
                if t.char_direcao == '>':                    
                    self.maquina.moverDireita(t.lst_simbsD)
                else:
                    self.maquina.moverEsquerda(t.lst_simbsD)
                self.estadoAtual = t.char_estadoPosterior
        
        return noPath  
        
