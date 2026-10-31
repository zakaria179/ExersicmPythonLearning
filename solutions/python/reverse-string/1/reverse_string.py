def reverse(text):
    reversed=[]
    index=-1
    while index > -(len(text)+1):
        reversed.append(text[index])
        index-=1
    return "".join(reversed)
        
        
        
