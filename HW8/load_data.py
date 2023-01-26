from input_data import staff

# получение данных из файла и формирование списка списков
def load_data_employee(name, staff):
    with open(name, encoding='utf-8') as file:
        a = [line.strip() for line in file]
        array = []
        for i in a:
            array.append(i.split())
        for i in array:
            for j in i:
                print([j][0])
    # return staff

print(load_data_employee('employee.txt', staff))