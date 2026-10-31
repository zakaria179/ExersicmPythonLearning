def is_valid(isbn):
    numbers=['0','1','2','3','4','5','6','7','8','9']
    isbn_digits = []
    for index ,char in enumerate(isbn):
        if char in numbers :
            isbn_digits.append(int(char))
        elif char =='X' and index == len(isbn)-1:
            isbn_digits.append(10)
        elif char == '-':
            continue
        else:
            return False
    if len(isbn_digits) != 10:
        return False
        
    
    count = 10
    result = 0
    for num in isbn_digits:
        result+=num*count
        count-=1
    return result%11==0
