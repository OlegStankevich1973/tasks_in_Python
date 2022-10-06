# 	Задайте список из вещественных чисел. Напишите программу, 
#     которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] = > 0.19
# lst = [1.1, 1.2, 3.1, 5, 10.01]
# lst_result = []
# for i in range (len(lst)):
#     while i < len(lst):
#        lst_result = (lst[i] * 1000) % 1000
       
#     i += 1
# print(lst_result)

from random import uniform #вызываем библиотеку создания дробных чисел
n = int(input('Введите размер списка '))
get_real_nums = [] #создаем список
for i in range(n):
    f = uniform(0, 100)
    get_real_nums.append(round(f, 2)) #заполняем список дробными значениями (два знака после запятой)

def find_diff(get_real_nums):# метод поиска разности между макс и мин дробными значениями
    nums = [round(x - int(x), 2) for x in (get_real_nums)]
    print('max дробное значение = ' , max(nums))
    print ('min дробное значение = ', min(nums))
    return max(nums) - min(nums)
   
print(get_real_nums)
print(find_diff(get_real_nums))


