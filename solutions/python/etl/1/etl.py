def transform(legacy_data):
    data = dict()
    for key in legacy_data:
        for char in legacy_data[key]:
            data[char.lower()]=data.get(char.lower(),key)
    return data 
