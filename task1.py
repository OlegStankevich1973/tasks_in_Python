#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#Примеры:
#6,78 -> 7
#5 -> нет
#0,34 -> 3
#=======================================================================
n = int(input())
if n == int(n):
    print('нет')
else:
    print(int(n * 10) % 10)

