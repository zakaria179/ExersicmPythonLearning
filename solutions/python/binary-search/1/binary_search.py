def find(search_list, value):
    length = len(search_list)

    if length == 0:
        raise ValueError("value not in array")

    middle = length // 2

    if search_list[middle] == value:
        return middle

    elif value > search_list[middle]:
        return middle + 1 + find(search_list[middle + 1:], value)

    else:
        return find(search_list[:middle], value)