def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes","jump"]
    binary_list = list(binary_str)
    binary_list.reverse()
    sequence = []
    for index , bin in enumerate(binary_list):
        if bin == '1' and index != 4 :
            sequence.append(actions[index])
        elif bin == '1' :
            sequence.reverse()
    return sequence
            
            
            
        
