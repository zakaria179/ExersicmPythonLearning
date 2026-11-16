def egg_count(display_value):
    binary_value = format(display_value,'b')
    somme = 0
    for bit in binary_value:
        somme+=int(bit)
    return somme
        
