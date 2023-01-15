# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def Main ():
    print (Factorization (int(input("Для получения списка простых множителей ввидите его: "))))
    print('Для завершения работы программы нажмите Enter'), input()

def Factorization (n): # метод выводит список простых множителей числа N
    result = [] # сюда складываем множители
    curNum = n # число, у которого осталось найти множители
    probe = 2 # число, на которое пытаемся делить
    while curNum != 1:
        if curNum % probe != 0: # проверены все множители из [2; probe]
            probe += 1
        else: # делим пока делится
            curNum /= probe
            result.append(probe)
        #   result = result + [probe]
    return result

Main()