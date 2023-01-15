def Main():
    data = list(open_file_as_str('data.txt'))
    code = rle_code(data)
    print('RLE code:', end=' '); rle_str(code)
    print()
    print(f'RLE uncode: {rle_decode(code)}')
    n = (rle_decode(code))
    write_file('RLE.txt', n)

def open_file_as_str(name): # чтение файла в строку
    with open(name, 'r') as f:
        line_list = f.readlines()
    return ''.join(line_list)

def rle_code(array): # получение списка кортежей (число, буква)
    result = []
    if array:
        current = array.pop(0)
        counter = 1
        for el in array:
            if el == current:
                counter += 1
            else:
                result.append((counter, current))
                current = el
                counter = 1
        result.append((counter, current))
    return result

def rle_str(r): # печать списка кортежей в виде строки
    for i in range(len(r)): 
        for j in range(len(r[i])):
                print(r[i][j], end = '')

def rle_decode(array):
    result = []
 
    for item in array:
        result.append(item[1] * item[0])
 
    return "".join(result)

def write_file(file, n): # запись в файл
    result = open(file, "w")
    result.write(n)
    result.close()

Main()