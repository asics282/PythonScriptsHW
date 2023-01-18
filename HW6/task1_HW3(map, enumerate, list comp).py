'''Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

#БЫЛО
from random import randint

def Main():
    n = int(input('Задайте длину списка, вводом числа N: '))
    random_list = ListAdd(n)
    print(f'Сгенерирован список случайных чисел от 1 до 10: {random_list}')
    print(f'Сумма элементов списка {random_list}, стоящих на нечетных позициях равна: {SumElementsFromOddIndex(random_list)}')
    print('Для завершения работы программы нажмите Enter'), input()

def ListAdd(n): # метод задает список из n рандомных чисел
    my_list = []
    for i in range(n):
        my_list.append(randint(1, 10)) # рандомными числами от 1 до 10
    return my_list

def SumElementsFromOddIndex(array): # метод считает сумму элементов списка, имеющих НЕчетный индекс
    sum = 0
    for i in (array[1:(len(array)):2]):
        sum = sum + i
    return sum

Main()

#СТАЛО
# задаем список вводом элементов через клавиатуру с помощью функции map
array = list(map(int, input('Введите числа через пробел: ').split()))

# создание списка значений, стоящих на НЕЧЕТНЫХ позициях списка с помощью генератора списка и функции enumerate
a = [value for index, value in enumerate(array) if index % 2 != 0]
print(f'Сумма элементов списка {array}, стоящих на нечетных позициях равна: {sum(a)}')