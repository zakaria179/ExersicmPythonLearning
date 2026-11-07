def sum_of_multiples(limit, multiples):
    multips=set()
    for item in multiples:
        count = item
        while count < limit and count !=0:
            multips.add(count)
            count+=item
    return sum(multips)            
            
