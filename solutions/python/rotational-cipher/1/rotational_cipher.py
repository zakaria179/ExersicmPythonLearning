def rotate(text, key):
    plain_lower = "abcdefghijklmnopqrstuvwxyz"
    cipher_lower = plain_lower[ key : ] + plain_lower[ : key ]
    plain_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_upper = plain_upper[ key : ] + plain_upper[ : key ]
    rot_text =''
    for char in text:
        if char in plain_lower:
            rot_text+=cipher_lower[plain_lower.index(char)]
        elif char in plain_upper:
            rot_text+=cipher_upper[plain_upper.index(char)]
        else:
            rot_text+=char
    return rot_text
            
