#	Реализуйте алгоритм перемешивания списка.
import random #Вызываем метод из библиотеки
test_list = input('Введите данные ')
print("Оригинальный список : "+ str(test_list))
res = random.sample(test_list, len(test_list)) # перемешиваем список (список,длина(список))
print("Перемешанный список : " + str(res))
