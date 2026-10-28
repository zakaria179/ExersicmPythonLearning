def is_armstrong_number(number):
    list_number = str(number)
    somme = 0
    for chiffre in list_number:
        somme +=int(chiffre)**len(list_number)
    return somme == number
        
        
