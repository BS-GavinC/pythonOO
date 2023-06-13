
class Animal:

    def __init__(self, name, size, weight, sex, age, arrived):
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__sex = sex
        self.__age = age
        self.__arrived = arrived
        self.__deathRate = 0
        self.__isDead = False


    @property
    def name(self):
        return self.__name;

    @name.setter
    def name(self, value):
        self.__name = value;

    @property
    def size(self):
        return self.__size;

    @size.setter
    def size(self, value):
        self.__size = value;

    @property
    def weight(self):
        return self.__weight;

    @weight.setter
    def weight(self, value):
        self.__weight = value;

    @property
    def sex(self):
        return self.__sex;

    @property
    def age(self):
        return self.__age;

    @age.setter
    def age(self, value):
        self.__age = value;

    @property
    def humanAge(self):
        pass

    @property
    def arrived(self):
        return self.__arrived
    
    @property
    def deathRate(self):
        return self.__deathRate;

    @deathRate.setter
    def deathRate(self, value):
        self.__deathRate = value;

    @property
    def isDead(self):
        return self.__isDead;

    @isDead.setter
    def isDead(self, value):
        self.__isDead = value;

    def Crier(self) -> str:
        return "Son commun d'un animal inidentifiable."

    def __str__(self) -> str:
        return f"il s'appelle {self.name}, il fait {self.size} cm et {self.weight} Kg. \n C'est un {self.sex} de {self.age} ans ({self.humanAge} années humaines). il est arrivé le {self.arrived}"
       