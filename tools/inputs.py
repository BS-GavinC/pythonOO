def askInteger(sentence) -> int:

    value = "-1"

    while(not value.isdigit()):
        value = input(sentence)

    return int(value);

def askFloat(sentence) -> float:
    while(True):
        try:
            value = float(input(sentence))
            return value;
        except:
            print("Valeur invalide, ressayez.")