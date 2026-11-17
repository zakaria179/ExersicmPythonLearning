def append(list1, list2):
    return list1+list2


def concat(lists):
    l = []
    for element in lists:
        l=append(l,element)
    return l 


def filter(function, list):
    l=[]
    for element in list:
        if function(element):
            l.append(element)
    return l
        


def length(list):
    count = 0
    for element in list:
        count +=1
    return count
        


def map(function, list):
    l = []
    for elemm in list:
        l.append(function(elemm))
    return l
        


def foldl(function, list, initial):
    accumulateur = initial
    for element in list:
        accumulateur=function(accumulateur,element)
    return accumulateur
        


def foldr(function, list, initial):
    return foldl(function,reverse(list),initial)


def reverse(list):
    return list[::-1]
