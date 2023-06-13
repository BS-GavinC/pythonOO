
from Models.Animal import Animal


class Cat(Animal):

    def __init__(self, name, size, weight, sex, age, arrived, personnality, clawCut, longHair):
        super().__init__(name, size, weight, sex, age, arrived)
        self.deathRate = 0.5
        self.__personnality = personnality
        self.__clawCut = clawCut
        self.__longHair = longHair

    @property
    def personnality(self):
        return self.__personnality;

    @personnality.setter
    def personnality(self, value):
        self.__personnality = value;

    @property
    def clawCut(self):
        return self.__clawCut;

    @clawCut.setter
    def clawCut(self, value):
        self.__clawCut = value;

    @property
    def longHair(self):
        return self.__longHair;

    @property
    def humanAge(self):
        return self.age * 11;

    def Crier(self):
        return "Miaouw Miaouw"

    def __str__(self) -> str:
        claw = "il a les griffes coupées" if self.clawCut else "il n'a pas les griffes coupées"
        longhair = "il a de longs poils" if self.longHair else "il n'a pas de longs poils"
        return "C'est un chat, " +  super().__str__() + f" Il est {self.personnality}, {claw}, {longhair}. "

    
