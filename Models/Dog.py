

from Models.Animal import Animal


class Dog(Animal):

    def __init__(self, name, size, weight, sex, age, arrived, collarColor, race, trained):
        super().__init__(name, size, weight, sex, age, arrived)
        self.deathRate = 1
        self.__collarColor = collarColor
        self.__race = race
        self.__trained = trained

    @property
    def collarColor(self):
        return self.__collarColor;

    @collarColor.setter
    def collarColor(self, value):
        self.__collarColor = value;

    @property
    def race(self):
        return self.__race;

    @property
    def trained(self):
        return self.__trained
    
    @trained.setter
    def trained(self, value):
        self.__trained = value;

    @property
    def humanAge(self):
        return self.age * 7;

    def Crier(self):
        return "Wouf Wouf"

    def __str__(self) -> str:
        train = "il est entrainé" if self.trained else "il n'est pas entrainé"
        return "C'est un chien " + super().__str__() + f" C'est un {self.race}, son collier est de couleur {self.collarColor}, {train}."

    