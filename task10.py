# 	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# Входные данные	Выходные данные
# 1 5 2 4 3	        5 4

ist = [int(i) for i in input("Введите числа через пробел: ").split()]

for i in range(0, len(ist) - 1):
    if ist[i] < ist[i+1]:
        print(ist[i+1])
