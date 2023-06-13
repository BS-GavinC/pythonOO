from Models.Bird import Bird
from Models.Cat import Cat
from Models.Dog import Dog
from tools.inputs import askFloat, askInteger


class PetShop:

    def __init__(self) -> None:
        self.__animals = [];
    
    @property
    def animals(self) -> list:
        return self.__animals

    def AskAnimalData(self) -> dict:

        values = {}

        values["name"] = input("Entrez le nom de l'animal : ")
        values["size"] = askInteger("Entrez la taille en cm de l'animal : ")
        values["weight"] = askFloat("Entrez le poids en Kg de l'animal : ")
        values["sex"] = input("Entrez le sexe de l'animal : ")
        values["age"] = askInteger("Entrez l'age en années de l'animal : ")
        values["arrived"] = input("Entrez la date d'arrivée de l'animal : ")

        return values;

    def RegisterBird(self):
        values = self.AskAnimalData();
        values["color"] = input("Entrez la couleur de l'oiseau : ")
        values["aviary"] = input("Necessite t'il une voliere ? y/-") == "y"
        self.animals.append(Bird(values["name"], values["size"], values["weight"], values["sex"], values["age"], values["arrived"], values["color"], values["aviary"]))
        print(self.animals)

    def RegisterCat(self):
        values = self.AskAnimalData()
        values["personnality"] = input("Entrez le caractere du chat : ")
        values["clawCut"] = input("Est-ce que les griffes sont coupées ? y/-") == "y"
        values["longHair"] = input("Le chat a t'il des poils longs ? y/-") == "y"
        self.animals.append(Cat(values["name"], values["size"], values["weight"], values["sex"], values["age"], values["arrived"], values["personnality"], values["clawCut"], values["longHair"]))
        print(self.animals)

    def RegisterDog(self):
        values = self.AskAnimalData();
        values["collarColor"] = input("Quel est la couleur du collier du chien : ")
        values["race"] = input("Quel est la race du chien : ")
        values["trained"] = input("Le chien est il entrainé ? y/-") == "y"
        self.animals.append(Dog(values["name"], values["size"], values["weight"], values["sex"], values["age"], values["arrived"], values["collarColor"], values["race"], values["trained"]))
        print(self.animals)