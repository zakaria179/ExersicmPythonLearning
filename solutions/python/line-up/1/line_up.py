def line_up(name, number):
    str_number = str(number)
    suffix = ""
    if len(str_number)==1:
        match str_number[0]:
            case '1':
                suffix+="st"
            case '2':
                suffix+="nd"
            case '3':
                suffix+="rd"
            case _:
                suffix+="th"
    else :
        if str_number[-2]=='1':
                suffix+="th"
        else :
            match str_number[-1]:
                case '1':
                    suffix+="st"
                case '2':
                    suffix+="nd"
                case '3':
                    suffix+="rd"
                case _:
                    suffix+="th"
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
