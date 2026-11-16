alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rows(letter):
    rank = alphabets.index(letter)
    size = (rank+1)*2 - 1
    result=[]
    middle = size//2
    for i in range(middle+1):
        line = list(" " * size)
        line[middle-i] = alphabets[i]
        line[middle+i] = alphabets[i]
        line = "".join(line)
        result.append(line)
    result_copy = reversed(result[:-1])
    for line in result_copy:
        result.append(line)
        
    return result 
        
    
