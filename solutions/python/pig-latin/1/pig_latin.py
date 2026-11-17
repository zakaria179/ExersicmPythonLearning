def rule_2_4(text):
    vowels={'a','e','i','o','u'}
    remain = ""
    for index , char in enumerate(text):
        if char in vowels or char == 'y':
            return text[index:]+remain+"ay"
        remain+=char


        
def translate(text):
    list_text = text.split(" ")
    returned_text = []
    for item in list_text:
        returned_text.append(trans(item))
    return " ".join(returned_text)
        

            
        
        
        
def trans(text):
    vowels={'a','e','i','o','u'}
    # rule 1 :
    if text[:2]=="xr" or text[:2]=="yt" or text[0] in vowels:
        return text+"ay"

    if "qu" in text:
        rem = ""
        for index, char in enumerate(text):
            vowels={'a','e','i','o','u'}
            if char == 'q' and text[index+1]=='u':
                return text[index+2:]+rem+"quay"
            if char in vowels:
                return rule_2_4(text)
            rem+=char

            
        
        
    # rule 2 and 4 :
    remain = ""
    for index , char in enumerate(text):
        if char in vowels :
            return text[index:]+remain+"ay"
        remain+=char

    remain = ""
    for index , char in enumerate(text):
        if char == 'y':
            return text[index:]+remain+"ay"
        remain+=char
    
