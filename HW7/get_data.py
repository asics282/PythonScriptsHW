from func_block import func_chunk
# получение данных из файла и формирование списка
def get_data(name):
    with open(name, encoding='utf-8') as file:
        if '\n' not in file.readlines():
            with open(name, encoding='utf-8') as file:
                a = [line.strip() for line in file]
                array = []
                for i in a:
                    array.append(i.split())
                return array
        else:
            with open(name, encoding='utf-8') as file:
                a2 = [line.strip() for line in file]
                temp = []
                for i in a2:
                    if i != '':
                        temp.append(i)
                return list(func_chunk(temp, 4)) # создание списка на равные части, состоящего из n элементов

# print(get_data('input_data1.txt'))