# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример:
# 2*x^2 + 4*x + 5 = 0 
# 5*x^2 + 2*x + 43 = 0
# Результат: 7*x^2 + 6*x + 48 = 0

def Main():
    print('!!!Программа для рассчета суммы многочлена с ПОЛОЖИТЕЛЬНЫМИ коеффициентами!!!')

    ReadFiletoPrint('polynomial1.txt')
    ReadFiletoPrint('polynomial2.txt')
    
    polinomial1 = (ReadFileToList('polynomial1.txt')) # список элементов строки в первом файле через пробел
    polinomial2 = (ReadFileToList('polynomial2.txt')) # список элементов строки в первом файле через пробел

    # создание списка списков
    list1 = ListStrToListNum(polinomial1) 
    list2 = ListStrToListNum(polinomial2)

    sum_coef1 = sum(Coef(list1, 0) + Coef(list2, 0)) #сумма коэффициентов второго члена многочлена
    sum_coef2 = sum(Coef(list1, 2) + Coef(list2, 2)) #сумма коэффициентов второго члена многочлена
    sum_free_coef = sum(Coef(list1, 4) + Coef(list2, 4)) #сумма коэффициентов второго члена многочлена
    summa = f'{sum_coef1}*x^2 + {sum_coef2}*x + {sum_free_coef} = 0'

    WriteFile('result.txt', summa)
    print("Программа посчитала сумму многочленов и записала их в файл result.txt")

def ReadFiletoPrint(file):
    file = open(file, "r")
    print(file.read())
    file.close

def ReadFileToList(file): # "читает" файл и создает список, с элементами "строчки" (элементы в строке через пробел)
    array = []
    with open(file, "r") as f: # чтоб не закрывать файл дополнительным кодом
        array = f.read().split() # в список помещаются элементы строки, разделенные пробелом
    return array

def ListStrToListNum(array): # функция создает список списков (элементов списка)
    array2 = []
    for i in array:
        array2.append(list(i))
    return (array2)

def Coef(array, n):
    array2 = []
    array3 = []
    for elem in array[n]:
        if elem == "*":
            break
        else:
            array2.append(elem)
    array3.append(int(''.join(array2)))
    return array3

def WriteFile(file, n): # запись сумму многочленов в файл
    result = open(file, "w")
    result.write(n)
    result.close()

Main()