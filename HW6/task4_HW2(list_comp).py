'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.'''

#БЫЛО
n = int(input('Введите число: '))

def ListAdd(n): # метод задает список из N элементов, заполненных числами из промежутка [-N, N]
    my_list = []
    for i in range(-n, n+1):
        my_list.append(i)
    return my_list

list_add = ListAdd(n)
#print(list_add) # можно раскоментить для проверки печати списка

def ReadFile(): # метод "читает" файл и создает список, в котором будут храниться позиции
    read_list = []
    with open("file.txt", "r") as f: # чтоб не закрывать файл дополнительным кодом
        for line in f:
            read_list.append(int(line))
    return read_list

position_list = ReadFile()

position1 = int(position_list[0]) 
position2 = int(position_list[1])

def PositionMultiplication (position1, position2, my_list): # метод печатает произведение элементов на указанных позициях
    result = int(my_list[position1-1]*my_list[position2-1])
    return print(f'Произведение элементов на позициях {position1} и {position2} в списке {my_list} равно {result}')

PositionMultiplication(position1, position2, list_add)

#СТАЛО
def Main():
    n = int(input('Введите число: '))
    my_list = [i for i in range(-n, n+1)]
    position = (ReadFile("file.txt"))
    result = (my_list[position[0]-1]*my_list[position[1]-1])
    print(f'Произведение элементов на позициях {position[0]} и {position[1]} в списке {my_list} равно {result}')

def ReadFile(name): # метод "читает" файл и создает список, в котором будут храниться позиции
    with open(name, "r") as f: # чтоб не закрывать файл дополнительным кодом
        return [int(line) for line in f]
         
Main()