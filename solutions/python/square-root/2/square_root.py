def square_root(number):
    percision=100
    iteration_inside = 1
    iteration_outside = 0 
    while percision > 0 :
        iteration_outside = 1/2 * ( iteration_inside + number / iteration_inside)
        iteration_inside = iteration_outside
        percision-=1
    return iteration_outside
    
