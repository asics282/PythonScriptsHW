def Main():
    data = list(open_file_as_str('data.txt'))
    code = rle_code(data)
    print(f'RLE code: {rle_str(code)}')
    write_file('RLE.txt', rle_str(code))

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

def rle_str(r): # печать кортежа в виде строки
    rle = []
    rle_str = []
    for i in range(len(r)): 
        for j in range(len(r[i])):
                rle.append(r[i][j])
    for k in rle:
        rle_str.append(str(k))
    return ''.join(rle_str)

def write_file(file, n): # запись в файл
    result = open(file, "w")
    result.write(n)
    result.close()

Main()