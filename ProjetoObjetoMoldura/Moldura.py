class Moldura:
    
    def __init__(self):
        self.__altura = 0
        self.__largura = 0

    def getAltura(self):
        return self.__altura
    
    def setAltura(self, altura):
        self.__altura = altura

    def getLargura(self):
        return self.__largura
    
    def setLargura(self, largura):
        self.__largura = largura

    def toString(self):
        print(f"A moldura tem {self.getAltura()}cm de altura por {self.getLargura()}cm de largura.")
    