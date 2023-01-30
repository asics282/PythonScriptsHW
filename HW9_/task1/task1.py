# Игра "Крестики-Нолики" c виртуальным окружением и PIP
from colorama import * # импорт библиотеки для печати цветного текста с предварительной установкой pip install colorama
init()
from random import randint

print(Style.BRIGHT + Back.CYAN + 'Игра "Крестики-Нолики"' + Style.RESET_ALL) # цветной вывод названия игры жирным шрифтом
print("Ознакомтесь c координатами игрового поля")
print('  0 1 2', '0 * * *', '1 * * *', '2 * * *', sep='\n')

field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] # игровое поле

def G(): # жеребьевка первого хода
    queue = randint(1, 2) # жеребьевка
    if queue == 1:
        return 'X'
    else:
        return 'O'
sign = G()
print(f'Первыми ходят {sign}')

def PrintField(): # вывод игрового поля
    for i in range(len(field)): 
        for j in range(len(field[i])):
            if j != 2:
                print(field[i][j], end = ' ')
            else:
                print(field[i][j], end = '\n')

def ChangeCourse(player): # смена очередности хода
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def Win(): # проверка на победу
    if(
        # проверка победы в строках
        (field[0] == [Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL]) or
        (field[1] == [Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL]) or
        (field[2] == [Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL, Fore.BLUE + 'X' + Style.RESET_ALL]) or
        # проверка победы в столбцах
        (field[0][0] == Fore.BLUE + 'X' + Style.RESET_ALL and field[1][0] == Fore.BLUE + 'X' + Style.RESET_ALL and field[2][0] == Fore.BLUE + 'X' + Style.RESET_ALL) or
        (field[0][1] == Fore.BLUE + 'X' + Style.RESET_ALL and field[1][1] == Fore.BLUE + 'X' + Style.RESET_ALL and field[2][1] == Fore.BLUE + 'X' + Style.RESET_ALL) or
        (field[0][2] == Fore.BLUE + 'X' + Style.RESET_ALL and field[1][2] == Fore.BLUE + 'X' + Style.RESET_ALL and field[2][2] == Fore.BLUE + 'X' + Style.RESET_ALL) or
        # проверка победы в диагоналях
        (field[0][0] == Fore.BLUE + 'X' + Style.RESET_ALL and field[1][1] == Fore.BLUE + 'X' + Style.RESET_ALL and field[2][2] == Fore.BLUE + 'X' + Style.RESET_ALL) or
        (field[0][2] == Fore.BLUE + 'X' + Style.RESET_ALL and field[1][1] == Fore.BLUE + 'X' + Style.RESET_ALL and field[2][0] == Fore.BLUE + 'X' + Style.RESET_ALL)
    ):
        return 'X'
    elif(
        # проверка победы в строках
        (field[0] == [Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL]) or
        (field[1] == [Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL]) or
        (field[2] == [Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL, Fore.RED + 'O' + Style.RESET_ALL]) or
        # проверка победы в столбцах
        (field[0][0] == Fore.RED + 'O' + Style.RESET_ALL and field[1][0] == Fore.RED + 'O' + Style.RESET_ALL and field[2][0] == Fore.RED + 'O' + Style.RESET_ALL) or
        (field[0][1] == Fore.RED + 'O' + Style.RESET_ALL and field[1][1] == Fore.RED + 'O' + Style.RESET_ALL and field[2][1] == Fore.RED + 'O' + Style.RESET_ALL) or
        (field[0][2] == Fore.RED + 'O' + Style.RESET_ALL and field[1][2] == Fore.RED + 'O' + Style.RESET_ALL and field[2][2] == Fore.RED + 'O' + Style.RESET_ALL) or
        # проверка победы в диагоналях
        (field[0][0] == Fore.RED + 'O' + Style.RESET_ALL and field[1][1] == Fore.RED + 'O' + Style.RESET_ALL and field[2][2] == Fore.RED + 'O' + Style.RESET_ALL) or
        (field[0][2] == Fore.RED + 'O' + Style.RESET_ALL and field[1][1] == Fore.RED + 'O' + Style.RESET_ALL and field[2][0] == Fore.RED + 'O' + Style.RESET_ALL)
    ):
        return 'O'
    else:
        return None

def InputSign(): #ввод координат и вставка в двумерный массив
    global sign
    count = 0
    while Win() == None:
        print(f'Xoдят {sign}')
        coor1, coor2 = int(input('Введите координату по горизонтале: ')), int(input('Введите координату по вертикале: '))
        if sign == 'X':
            field[coor1][coor2] = Fore.BLUE + 'X' + Style.RESET_ALL # за крестиками закреплен синий цвет
        else:
            field[coor1][coor2] = Fore.RED + 'O' + Style.RESET_ALL # за ноликами закреплен красный цвет
        PrintField()
        count += 1
        sign = ChangeCourse(sign) # смена знака (хода) X <=> Y
        if count == 9 and Win() == None:
            print('Ничья')
            break
        elif Win() == 'O':
            print(Style.BRIGHT + Fore.RED + 'Победили O')
            break
        elif Win() == 'X':
            print(Style.BRIGHT + Fore.BLUE + 'Победили X')
            break

InputSign()