# здесь в словаре храниться телефонный справочник
from get_data import get_data
from input_data import input_data
array = get_data('input_data1.txt')
# new_array = (input_data()) # ввод новой записи

# конверсия списка списков в словарь, где ключом является первый элемент каждого из списка
def two_dim_array_to_dict (array):
    my_dict = {}
    for i in range(len(array)):
        my_dict[array[i][0]] = (" ".join(array[i][1:])) # словарь, где ключом является первый элемент каждого из списка
    return my_dict

d = two_dim_array_to_dict(array)

# # добавление новой записи в словарь (справочник)
# def add_new_note()
# d[new_array[0]] = (" ".join(new_array[1:])) 

# печать словоря
def print_dict():
    for i in d:
        print(i, d[i])