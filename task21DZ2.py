#Задайте список из n чисел последовательности(1+1/n) ** n выведите на экран их сумму.

n = int(input('Введите количество чисел в списке '))

def numbers(n):#название функции
    sum = 0
    for i in range(n):
        a = int(input(f'Введи число {i + 1} '))# Вводим числа для расчета значений по формуле
        a = (1 + 1 / a)**a
        sum = a + sum
        i += 1
    return sum #возвращаем полученное значение в начало

print('Сумма чисел равна',round((numbers(n)), 2))#округляем ответ до двух знаков после запятой