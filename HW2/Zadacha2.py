""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

number = int(input('Введите число: '))

def product (number): # метод для расчета произведения чисел от 1 до number
    if number == 1: # условие для выхода
        return 1
    else:
        return number * product(number - 1)

def PrintResult(number): # метод для печати произведения чисел от 1 до number
    list = []
    for k in range(1, number + 1):
        list.append(product(k))
    return list

result = PrintResult(number)

print(f"N = {number}, тогда {result}")