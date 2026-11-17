def is_pangram(sentence):
    sentence=sentence.lower()
    set_of_sentence = set(sentence)
    alphabets="abcdefghijklmnopqrstuvwxyz"
    set_of_alphabets=set(alphabets)
    count = 0
    for item in set_of_sentence:
        if item in set_of_alphabets:
            count+=1
    return count ==26
        
