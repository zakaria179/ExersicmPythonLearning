def score(x, y):
    dart=pow(x**2 + y**2 , 0.5)
    if dart <=1.0:
        return 10
    if dart <= 5.0:
        return 5
    if dart <= 10.0:
        return 1
    return 0
        
    
