def is_isogram(phrase):
    phrase=phrase.lower()
    alphabets="abcdefghijklmnopqrstuvwxyz"
    count_alphabets=dict()
    count=0
    set_of_phrase = set(phrase)
    for char in set_of_phrase:
        if char in alphabets:
            count +=1
    for char in phrase:
        if char in alphabets:
            count_alphabets[char]=count_alphabets.get(char,0)+1
    return sum(count_alphabets.values())==count 
            
        
