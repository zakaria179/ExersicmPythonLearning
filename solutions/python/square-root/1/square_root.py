def square_root(number):
    n=100
    x_0 = 1
    x_1 = 0 
    while n > 0 :
        x_1 = 1/2 * ( x_0 + number / x_0)
        x_0 = x_1
        n-=1
    return x_1
    
