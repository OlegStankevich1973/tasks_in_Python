#  Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141. 10^(-1) <= d10 <= 10^(-10)
# формула ряда Лейбница pi = 4*(sum(((-1)**x)/(2*x+1)

# # Ряд Лейбница
d = int(input("Введите число для заданной точности числа Пи: "))
n = 10000000 #количество сложений
x = 0 
my_pi = 4*(sum(((-1)**x)/(2*x+1) for x in range(n)))
print (round(my_pi,d))
