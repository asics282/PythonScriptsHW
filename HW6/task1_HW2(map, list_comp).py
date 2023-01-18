""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0.56 -> 11 """

# # БЫЛО
number = float(input('Введите число: '))

def SumDightsFloat(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum

sum_dights_float = (SumDightsFloat(number))
print(f"Сумма цифр вещественного числа {number} равна {sum_dights_float}")

# СТАЛО
list_dight = [i for i in (input('Введите число: ')) if i != '.']
print(f'Сумма цифр, введенного вами вещественного числа равна {sum(list(map(int, list_dight)))}')