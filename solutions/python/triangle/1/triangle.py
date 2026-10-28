def equilateral(sides):
    if sides[0]==sides[1]==sides[2]!=0:
        if degenerate(sides):
            return True
    return False

def isosceles(sides): 
    if sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]:
        if degenerate(sides):
            return True
    return False
    
def scalene(sides):
    if sides[0]!=sides[1] and sides[0]!=sides[2] and sides[1]!=sides[2]:
        if degenerate(sides):
            return True
    return False
        
    

def degenerate(sides):
    a,b,c=sides
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False
        
    
    
