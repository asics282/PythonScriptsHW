# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

player1 = input('Введите имя Игрока №1: ')
player2 = input('Введите имя Игрока №2: ')
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
    k = int(input(f'{player} введите количество конфет, которое хотите забрать: '))
    if k in range(1, 29):
        amount = amount - k
        print(f'На столе осталось {amount} конфет')
        player = ChangeCourse(player, player1, player2)
    else:
        print('Введите число от 1 до 28')

print(f'Победил игрок {ChangeCourse(player, player1, player2)}')