def value(colors):
    return color_code(colors[0])*10+color_code(colors[1])
def color_code(color):
    dic_color={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
    return dic_color[color]

def label(colors):
    resistance_value=value(colors)*pow(10,color_code(colors[2]))
    if resistance_value//1000 >= 1000000: 
        return str( resistance_value // 1000000000 ) + " gigaohms"
    if resistance_value//1000 >= 1000:
        return str( resistance_value//1000000 ) + " megaohms"
    if resistance_value//1000 >= 1:
        return str( resistance_value//1000 ) + " kiloohms"
    else:
        return str( resistance_value ) + " ohms"
    
