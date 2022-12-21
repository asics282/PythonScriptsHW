# Задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

X, Y, Z = (input('Введите X: ')), (input('Введите Y: ')), (input('Введите Z: '))
if not (X or Y or Z) == (not X) and (not Y) and (not Z):
    print('True')
else:
    print('False')