# 	Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# 	k = 2 = > 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# метод составления формулы квадратного уравнения( пронимает на вход список[3,4 ,5])
from random import randint

def create_formula(factors):
    #  присваиваем переменную k длине списка меньше 1
    k = len(factors)-1
    # выходом из метода будет строка
    res = ""
    # проходим все элементы списка
    for i in range(0,len(factors)):
        # последний элемент строки
        if i == len(factors)- 1:
            # получает просто численное значение из входного списка
            res += f"{factors[i]}"
        
        elif k ==1:
            # присваиваем значение с х
            res += f"{factors[i]}x +"
        else:
            # присваиваем значения х со степенью к
            res += f"{factors[i]}x^{k} + "
        k -=1
    return res
def polinome(k, file_name):
    # формирует список коэфициентов случайное число из диапазона 0,k +1
    factors = [randint(1, 101) for k in range(0, k + 1)]
    res = create_formula(factors)
# print(create_formula([2,3,4,7]))
# метод принимает на вход значение степени равное количеству членов уравнения и значения с файлов
def polinome(k, file_name):
    # формирует список коэфициентов случайное число из диапазона 0,k +1
    factors = [randint(1, 101) for _ in range(0,k + 1)]
    res = create_formula(factors)
 
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(' '.join([str(i) for i in factors[::-1]]) + '\n')
        f.write(res)
polinome(3,'file1.txt')
with open('file1.txt')as f:
    factors1 = [int(i) for i in f.readline().split()]
   

