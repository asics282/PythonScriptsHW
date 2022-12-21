# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint
n = int(input('Задайте длину списка, вводом числа N: '))

def ListAdd(n): # метод задает список из n чисел
    my_list = []
    for i in range(n):
        my_list.append(randint(1, 10)) # рандомными числами от 1 до 10
        # my_list.append(i+1) # числами по порядку от 1 до n
    return my_list

random_list = ListAdd(n)

new_list = random_list[::-1] # переворачиваем исходный список

def MultyList (array, array2, n): # метод попарного элементов исходного списка
    array3 = []
    for i in range(n - (n//2)): # создание нового списка до необходимой длины
        array3.append(array[i]*array2[i])
    return array3

multy_list = MultyList (random_list, new_list, n)

print(f'Исходный список: {random_list}')
print(f'Попарноумноженный список: {multy_list}')
print('Для завершения работы программы нажмите Enter'), input()