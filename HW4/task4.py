# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
def Main():
    k = int(input('Введите натуральное число: '))
    members = ArrayDegree(k)
    print(f'Список членов со степенями: {members}') # вывод списка членов со степенями для контроля
    numbers = Coef(k)
    print(f'Список коэффициентов: {numbers}')
    result = (' + '.join(Sum(members, numbers))+str(' = 0')) # создаем из списка строку
    print(f'Сгенерирован многочлен: {result}') # вывод результата
    WriteFile("result1.txt", result)
    print(f"Программа создала многочлен {result} степени {k} и записала его в файл result1.txt")
    print('Для завершения программы нажмите Enter'), input()

def ArrayDegree(k): # создание списка членов многочлена с соответствующими степенями и пустой последней строкой (для свободного члена)
    array_degree = []
    for i in range (k, -1, -1):
        if i == 0:
            array_degree.append('')
        elif i == 1:
            array_degree.append(('x'))
        else:
            array_degree.append(('x^'+str(i)))
    return array_degree

def Coef(k): # создание списка коэффициентов многочлена
    array_numbers = []
    for i in range (k, -1, -1):
        array_numbers.append((str(randint(0, 10))))
    return array_numbers

def Sum(a, b): # создает новый список из элементов списка степеней и элементов списка коэффициентов НЕравных нулю
    summa = []
    i = 0
    for elem in a:
        if b[i] != "0": # если элемент списка НЕ совпадает с 0, то добавляем его в новый список
            summa.append(b[i] + elem)
        i+=1
    return summa

def WriteFile(file, n): # запись сумму многочленов в файл
    result = open(file, "w")
    result.write(n)
    result.close()

Main()