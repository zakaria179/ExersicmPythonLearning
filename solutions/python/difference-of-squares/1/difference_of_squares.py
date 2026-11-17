def square_of_sum(number):
    return pow((number*(number+1))//2,2)


def sum_of_squares(number):
    somme = 0
    for nums in range(1,number+1):
        somme +=nums**2
    return somme 
        


def difference_of_squares(number):
    return abs(square_of_sum(number)-sum_of_squares(number))
