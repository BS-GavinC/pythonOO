

from Models.PetShop import PetShop
from tools.inputs import askFloat, askInteger

ps = PetShop();

continuer = True;

while(continuer):
    selection = askInteger("1. Ajouter un animal \n2. Lister animaux.\n3. Compter animaux.\n4. Passer la nuit.\n5. Quitter.\nEntrez votre choix : ")

    match(selection):
        case 1:
            choix = askInteger("1. Chien.\n2. Chat\n3. Oiseau\nEntrez votre choix : ")
            match(choix):
                case 1: 
                    ps.RegisterDog()
                case 2:
                    ps.RegisterCat()
                case 3:
                    ps.RegisterBird()
                case _:
                    print("Choix incorrect. Renvoi au menu.")
        case 2:
            ps.ListAnimals();
        case 3:
            ps.HowManyAnimals();
        case 4:
            ps.PassNight();
        case 5:
            continuer = False;
        case _:
            print("Choix invalide. Reessayez.")
            break;

