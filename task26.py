# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.
# Чтобы найти НОК нескольких натуральных чисел, надо разложить эти числа на простые множители,
# затем взять из этих разложений каждый простой множитель с наибольшим показателем степени и 
# перемножить эти множители между собой
#99 = 3*3*11 = 3**2*11
# 54 = 2*3*3*3 = 2 3**3
# 2*11*3**3 = 594
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
if a > b:
    num = a
else:
    num = b
trigger = True
while trigger == True:
    if (num % a) == 0 and (num % b) == 0:
        trigger = False
    else:
        num += 1
print(num)
