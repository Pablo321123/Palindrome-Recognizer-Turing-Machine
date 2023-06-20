from abstractFita import *

class Trilha(AbstractFita):
    def __init__(self, palavra) -> None:
        print(palavra)
        
    def moverDireita(self):
        return super().moverDireita()
    
    def moverEsquerda(self):
        return super().moverEsquerda()
    
    def getEstadoAtual(self):
        return super().getEstadoAtual()