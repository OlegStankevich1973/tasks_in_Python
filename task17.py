#	Удалить вторую цифру трёхзначного числа.
number = int(input('Ввведите данные '))
res = (((number // 100)*10) + (number % 10)) 

# или так

# n1 = number // 100
# n2 = number % 10
# res = n1 * 10 + n2
print(res)


