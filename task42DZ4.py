# 	Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint


def create_formula(factors):
    #  присваиваем переменную k длине списка меньше 1
    k = len(factors)-1
    # выходом из метода будет строка
    res = ""
    # проходим все элементы списка
    for i in range(0, len(factors)):
        # последний элемент строки
        if i == len(factors) - 1:
            # получает просто численное значение из входного списка
            res += f"{factors[i]}"

        elif k == 1:
            # присваиваем значение с х
            res += f"{factors[i]}x +"
        else:
            # присваиваем значения х со степенью к
            res += f"{factors[i]}x^{k} + "
        k -= 1
    return res


def polinome(k, file_name):
    # формирует список коэфициентов случайное число из диапазона 0,k +1
    factors = [randint(1, 101) for k in range(0, k + 1)]
    res = create_formula(factors)
# print(create_formula([2,3,4,7]))
# метод принимает на вход значение степени равное количеству членов уравнения и значения с файлов


def polinome(k, file_name):
    # формирует список коэфициентов случайное число из диапазона 0,k +1
    factors = [randint(1, 101) for _ in range(0, k + 1)]
    res = create_formula(factors)

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(' '.join([str(i) for i in factors[::-1]]) + '\n')
        f.write(res)


polinome(3, 'file1.txt')
polinome(3, 'file2.txt')
pol_1 = []
with open('file1.txt')as f1, open('file2.txt') as f2:
    factors1 = [int(i) for i in f1.readline().split()]
    factors2 = [int(i) for i in f2.readline().split()]
if len(factors1) > len(factors2):
    res = [a + b for a, b in zip(factors1, factors2)]
elif len(factors1) > len(factors2):
    res = factors1.copy()
    for i in range(len(factors2)):
        res[i] += factors2[i]
else:
    res = factors2.copy()
    for i in range(len(factors1)):
        res[i] += factors1[i]
with open('file_3.txt', 'w') as f:
    f.write(create_formula(res[::-1]))
