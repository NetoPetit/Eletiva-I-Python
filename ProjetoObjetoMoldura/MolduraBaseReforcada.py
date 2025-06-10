import Moldura

class Moldurabasereforcada(Moldura.Moldura):

    def __init__(self):
        super().__init__()

    def getAltura(self):
        return self.__altura
    
    def setAltura(self, altura):
        self.__altura = altura

    def getLargura(self):
        return self.__largura
    
    def setLargura(self, largura):
        self.__largura = largura

    def toString(self):
        print(f"A moldura com a base reforçada tem {self.getAltura()}cm de altura por {self.getLargura()}cm de largura.")