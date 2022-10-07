# Напишите функцию triangle(a, b, c), которая принимает на вход
# три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)
# Это треугольник
a = int(input())
b = int(input())
c = int(input())
def triangle(a, b, c):#метод определения треугольника
    flag = False
    if (a + b) > c and (b + c) > a and (a + c) > b:
       flag = True
       return"yes" if flag else"no"
print(triangle(a,b,c))