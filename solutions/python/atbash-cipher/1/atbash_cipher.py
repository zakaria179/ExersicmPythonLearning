ALPHABETS="abcdefghijklmnopqrstuvwxyz"
atbash_cipher=dict(zip(ALPHABETS,ALPHABETS[::-1]))
decod_cipher=dict(zip(ALPHABETS[::-1],ALPHABETS))

def encode(plain_text):
    plain_text=plain_text.lower()
    code=""
    count=0
    for char in plain_text:
        if char in ALPHABETS:
            code+=atbash_cipher[char]
            count+=1
            if count==5:
                code+=" "
                count=0
        elif char in ".,!:?" or char ==" ":
            continue
        else:
            code+=char
            count+=1
            if count==5:
                code+=" "
                count=0
    
    return code.strip()

def decode(ciphered_text):
    code=""
    for char in ciphered_text:
        if char in ALPHABETS:
            code+=decod_cipher[char]
        elif char in ".,!:?" or char ==" ":
            continue
        else:
            code+=char
    return code
            
            
        
        
