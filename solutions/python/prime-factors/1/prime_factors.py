def facteurs_premiers(n):
    facteurs = []
    diviseur = 2

    while n > 1:
        while n % diviseur == 0:
            facteurs.append(diviseur)
            n //= diviseur

        diviseur += 1

    return facteurs


def factors(value):
    facteurs = facteurs_premiers(value)
    return facteurs
    
