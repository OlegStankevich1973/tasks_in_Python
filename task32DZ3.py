# 	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 	45 -> 101101
# 	3 -> 11
# 	2 -> 10
a = int(input('Введите число '))
b = ' ' #создаем строку
while a > 0:
   
    b = str(a % 2) + b #заполняем строку 
    a = a // 2 #делим а для получения целого числа
print(b)
