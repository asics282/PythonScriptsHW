# Игра в конфеты против "умного" компьютера

from random import randint

player1 = input('Введите имя Игрока: ')
player2 = 'Компьютер'
amount = 2021 # общее количество конфет

def G(player1, player2): # жеребьевка первого хода
    queue = randint(1, 2) # жеребьевка
    if queue == 1:
        return player1
    else:
        return player2

player = G(player1, player2) # текущий игрок

print(f'Ход игрока {player}')

def ChangeCourse(player, player1, player2): # смена очередности хода
    if player == player1:
        player = player2
    else:
        player = player1
    return player

while amount > 0: 
    if player == player1: # ход игрока
        k = int(input(f'{player1} введите количество конфет, которое хотите забрать: '))
        if k in range(1, 29):
            amount = amount - k
            print(f'На столе осталось {amount} конфет')
            player = ChangeCourse(player, player1, player2)
        else:
            print('ВНИМАНИЕ! Введите число от 1 до 28')
    else: # ход компьютера
        if amount > 57:
            k1 = randint(1, 28)
            print(f'{player2} забрал {k1} конфет')
            amount = amount - k1
            print(f'На столе осталось {amount} конфет')
            player = ChangeCourse(player, player1, player2)
        elif amount in range (30, 58): # диапозон от 30 до 57 
            k1 = amount - 29 # делаем так, чтобы на столе всегда оставалось 29 конфет
            print(f'{player2} забрал {k1} конфет')
            amount = amount - k1
            print(f'На столе осталось {amount} конфет')
            player = ChangeCourse(player, player1, player2)
        else: # если осталось меньше 28 конфет
            k1 = amount
            print(f'{player2} забрал {k1} конфет')
            amount = amount - k1
            print(f'На столе осталось {amount} конфет')
            player = ChangeCourse(player, player1, player2)

print(f'Победил игрок {ChangeCourse(player, player1, player2)}')