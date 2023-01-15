from random import randint
# Игра "Крестики-Нолики"
print('Игра "Крестики-Нолики"')
print("Ознакомтесь координатами игрового поля")
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
        (field[0] == ['X', 'X', 'X']) or
        # проверка победы в столбцах
        (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X') or
        (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X') or
        (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X') or
        # проверка победы в диагоналях
        (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X') or
        (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X')
    ):
        return 'X'
    elif(
        # проверка победы в строках
        (field[0] == ['O', 'O', 'O']) or
        # проверка победы в столбцах
        (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O') or
        (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O') or
        (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O') or
        # проверка победы в диагоналях
        (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O') or
        (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O')
    ):
        return 'O'
    else:
        return None

def InputSign(): #ввод координат и вставка в двумерный массив
    global sign
    while Win() == None:
        print(f'Xодят {sign}')
        coor1, coor2 = int(input('Введите координату по горизонтале: ')), int(input('Введите координату по вертикале: '))
        if sign == 'X':
            field[coor1][coor2] = 'X'
        else:
            field[coor1][coor2] = 'O'
        PrintField()
        sign = ChangeCourse(sign) # смена знака (хода) X <=> Y
    print(f'Победили {Win()}')

InputSign()