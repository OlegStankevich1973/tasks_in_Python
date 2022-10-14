#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
 # На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
 # Выходные данные:          12W1B12W3B24W1B14W

# функция раскодировки строки
def coding(txt):
    count = 1
    res = ''
    # цикл считает одинаковые знаки в строке
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
# сравнивает последний и предпоследний элемент строки
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        # формирует строку из элементов
        res = res + str(count) + txt[-1]
    return res

# функция кодировки строки
def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
#  isalpha() возвращает True, если все символы в строке str являются буквенными и есть хотя бы один символ       
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
