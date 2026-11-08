"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 9
SUPERLIST = 10
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    if len(list_one)==len(list_two):
        for index,item in enumerate(list_one):
            if list_one[index]!= list_two[index]:
                return UNEQUAL
        else:
            return  EQUAL
    if len(list_one)<len(list_two):
        if not list_one:
            return SUBLIST
        for iteration in range(len(list_two)-len(list_one)+1):
            comparing_list = list_two[iteration:iteration+len(list_one)]
            if list_one==comparing_list:
                return SUBLIST
        else:
            return UNEQUAL
    if len(list_two)<len(list_one):
        if not list_two:
            return SUPERLIST
        for iteration in range(len(list_one)-len(list_two)+1):
            comparing_list = list_one[iteration:iteration+len(list_two)]
            if list_two==comparing_list:
                return SUPERLIST
        else:
            return UNEQUAL
    return UNEQUAL
    
