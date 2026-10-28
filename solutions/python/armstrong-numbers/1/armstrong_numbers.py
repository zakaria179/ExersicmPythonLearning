def is_armstrong_number(number):
    list_number = str(number)
    sum = 0
    for chiffre in list_number:
        sum +=int(chiffre)**len(list_number)
    return sum==number
        
        
