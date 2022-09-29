# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# Подсказка: можно использовать модуль datetime

from datetime import datetime #импортируем функцию datetime
# пропускаем по две строки вначале и в конце def

def num_random(n):
    # из функции datetime берем расширение microsecond
    number = datetime.now().microsecond
    return number % n # возвращаем остаток от деления на n
# пропускаем две строки

print(num_random(1000) )
