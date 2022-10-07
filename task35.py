# 	Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

lst = [i for i in range(10, 100)]
lst1 = filter(lambda x: not x % 9, lst)# filter работает только один раз, потом его надо повторять
print(list(lst1))
lst1 = filter(lambda x: not x % 9, lst)
lst2 = map(lambda x: x ** 2, lst1)
print(list(lst2))
lst1 = filter(lambda x: not x % 9, lst)
lst2 = map(lambda x: x ** 2, lst1)
print(sum(list(lst2)))


