def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 :
        raise ValueError("Classification is only possible for positive integers.")
    if aliquot(number)==number:
        return 'perfect'
    if aliquot(number)< number :
        return 'deficient'
    return 'abundant'

def aliquot(number):
    aliquot_sum = 0
    divisor=1
    for divisor in range(1,number):
        if number % divisor == 0 :
            aliquot_sum+=divisor
    return aliquot_sum
            
        
        
