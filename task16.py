#	Напишите программу, которая проверяет пятизначное число на палиндром.

# Вариант 1
# number = input('Ввведите данные ')
# print(number == number[::-1])

#Вариант 2
number = input('Ввведите данные ')
palindrome = True
for i in range(len(number)//2):# делим строку на 2 и проходим все элементы строки
    if number[i]!= number[-i - 1]:#сравниваем  0 элемент с -1
        palindrome = False
    # break
if palindrome:
    print('Палиндром')
else:
    print('Не палиндром')