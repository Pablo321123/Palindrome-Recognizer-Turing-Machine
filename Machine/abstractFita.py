from abc import ABC, abstractmethod


class AbstractFita(ABC):
    @abstractmethod
    def moverDireita(self):
        pass

    @abstractmethod
    def moverEsquerda(self):
        pass

    @abstractmethod
    def getEstadoAtual(self):
        pass
