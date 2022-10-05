# 	Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] = > [12, 15, 16]
# [2, 3, 5, 6] = > [12, 15]


# from random import randint
# sp = [2, 3, 4, 5, 6]
# result_sp = []
# for i in range((len(sp)+1)//2):#проходим список до половины
#     result_sp.append(sp[i]*sp[len(sp)-1-i])  # append добавляем значения в новый список перемножением первого элемента на последний 
# print(result_sp)

from random import randint
number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 100))#создаем рандомный список с числами от 0 до 100

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:#условие прохождения половин списка
        number = number - 1#последний элемент списка
        a = list[i] * list[number]
        list2.append(a) #добавляем в список 2 значения а
        i += 1
        
print(list)
print(list2)#условие прохождения половин списка
