def is_paired(input_string):
    open_brackets = {'[', '{', '('}
    closed_brackets = {')', '}', ']'}
    pile = []
    for char in input_string:
        if char in open_brackets:
            pile.append(char)
        elif char in closed_brackets:
            match char :
                case '}':
                    char = '{'
                case ')':
                    char = '('
                case ']':
                    char = '['
                case '_':
                    return False
            if not pile:
                return False
            if char == pile[-1]:
                pile.pop()
            else:
                pile.append(char)
    if not pile :
        return True
    return False