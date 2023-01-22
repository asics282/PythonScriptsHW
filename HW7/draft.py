with open('input_data1.txt', encoding='utf-8') as file:
    a = [line.strip() for line in file]
    print(a)
    temp = []
    for i in a:
        if i != '':
            temp.append(i)
    print(temp)


# ['Ивлева Виктория +79065129727 Супруга', 'Тарасов Алексей +79031238845 Начальник']