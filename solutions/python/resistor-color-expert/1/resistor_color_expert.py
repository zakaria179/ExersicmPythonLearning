def value(colors,bands):
    if bands == 4:
        return color_code(colors[0])*10+color_code(colors[1])
    return color_code(colors[0])*100 + color_code(colors[1])*10 + color_code(colors[2])
def color_code(color):
    dic_color={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
    return dic_color[color]
def label(colors):
    bands = len(colors)
    resistance_value=value(colors,bands)*pow(10,color_code(colors[-2]))
    if resistance_value//1000 >= 1000000 : 
        return str( resistance_value // 1000000000 if resistance_value % 1000000000 == 0 else resistance_value / 1000000000) + " gigaohms"
    if resistance_value//1000 >= 1000:
        return str( resistance_value // 1000000 if resistance_value % 1000000 == 0 else resistance_value / 1000000) + " megaohms"
    if resistance_value//1000 >= 1:
        return str( resistance_value // 1000 if resistance_value % 1000 == 0 else resistance_value / 1000) + " kiloohms"
    return str( resistance_value ) + " ohms"
def resistor_label(colors):
    tolerance = {"grey" : 0.05, "violet" : 0.1,"blue": 0.25,"green" :0.5,"brown" :1,"red" : 2,"gold" : 5,"silver" : 10}
    if len(colors)==1:
        return str(color_code(colors[0])) + " ohms"
    return label(colors)+" ±"+str(tolerance[colors[-1]])+"%"
        
    
    
