def cleaner(dict_list):
    dic_list = []
    dic = {}
    for item in dict_list:
        for key, value in item.items():
            key_striped = key.rstrip()
            key_striped = key_striped.lstrip()
            value_striped = value.lstrip()
            value_striped = value_striped.rstrip()
            dic[key_striped] = value_striped
        dic_list.append(dic)
        dic = {}
    return dic_list


