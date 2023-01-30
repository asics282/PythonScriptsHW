

# items = msg.split() # /act 123 + 534s

d = input('Ввод: ')
items = d.split()

if 'j' not in d:
    x = int(items[1])
    y = int(items[3])
else:
    x = complex(items[1])
    y = complex(items[3])

if items[2] == '+':
    print(x + y)

elif items[2] == '-':
    print(x - y)

elif items[2] == '*':
    print(x * y)

elif items[2] == '/':
    print(x * y)

else:
    print('Неизвестное действие')
