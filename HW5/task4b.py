def Main():
    array1 = OpenFileAsList('RLE.txt')
    array2 = OpenFileAsList('RLE.txt')
    ListDight(array1) # получение списка чисел
    ListLetter(array2) # получение списка букв
    result = ''.join(list(map(lambda x, y: x * y, ListDight(array1), ListLetter(array2))))
    print(result) # контроль результата
    WriteFile('RLE uncode.txt', result)

def OpenFileAsList(name): # чтение файла в строку
    with open(name, 'r') as f:
        line_list = f.readlines()
    return list(''.join(line_list))

def ListDight(array): # получение списка чисел
# получение строки, в которой буквы заменены на '!'
    for i in range(len(array)):
        if array[i].isdigit() == False:
            array[i] = '!'
    srt_array = ''.join(array)

    array_digit = (srt_array.split('!')) # получение списка с числами перед буквами
    array_digit.pop() # зная, что посл элемент точно была буква, а теперь '!', удаляем его
    return list(map(int, array_digit)) # возвращаем список с числами

def ListLetter(array): # получение списка букв
    # получение строки, в которой цифры заменены на '!'
    for i in range(len(array)):
        if array[i].isdigit() == True:
            array[i] = '!'
    # сбока списка, состоящего только из букв
    temp = []
    for i in array:
        if i != '!':
            temp.append(i)
    return temp

def WriteFile(file, n): # запись в файл
    result = open(file, "w")
    result.write(n)
    result.close()

Main()