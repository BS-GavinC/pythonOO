

from Models.Animal import Animal


class Bird(Animal):

    def __init__(self, name, size, weight, sex, age, arrived, color, aviary):
        super().__init__(name, size, weight, sex, age, arrived)
        self.deathRate = 3;
        self.__color = color
        self.__aviary = aviary


    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value;
    
    @property
    def aviary(self):
        return self.__aviary
    
    @aviary.setter
    def aviary(self, value):
        self.__aviary = value

    @property
    def humanAge(self):
        return self.age * 7.62;

    def Crier(self):
        return "Cui cui"

    def __str__(self) -> str:
        voliere = "necessite une" if self.aviary else "ne necessite pas de"
        return "C'est un oiseau, " + super().__str__() + f" il a les plumes {self.color}, et {voliere} voliere."