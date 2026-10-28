def find_anagrams(word, candidates):
    length_of_the_word =  len(word)
    word = word.lower()
    list_of_chars = sorted(word)
    anargams=[]
    for candidate in candidates :
        candidate1 = candidate.lower()
        if length_of_the_word == len(candidate1) and list_of_chars == sorted(candidate1) and candidate1 != word:
            anargams.append(candidate)
    return anargams
            
        
            
        
    
