#	Удалить вторую цифру трёхзначного числа.
number = int(input('Ввведите данные '))
res = (((number // 100)*10) + (number % 10)) 

# или так чисел

n1 = number // 100
n2 = number % 10
res = n1 * 10 + n2
print(res)

# или так для строк
number = input('Ввведите данные ')
print(number[0] + number[2])# складываем элементы строки

# или еще так для списков
number = list(str(123))
del number[1]
print(''.join(number)) #склеивает элементы списка

