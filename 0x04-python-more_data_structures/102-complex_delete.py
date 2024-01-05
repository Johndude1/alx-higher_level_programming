#!/usr/bin/python3
def complex_delete(a_dictionary, value):
<<<<<<< HEAD
list_keys = list(a_dictionary.keys())
    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]
=======
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

>>>>>>> e1131ebb30b51418fa62832f6430ee466f06f6a8
    return (a_dictionary)
