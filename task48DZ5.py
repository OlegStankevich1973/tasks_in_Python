# 	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

# б)Подумайте как наделить бота "интеллектом"


# вариант человек против человека:


from random import randint

# функция проверяет правильно ли взяли  конфеты
# def input_dat(name):
#     x = int(
#         input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# # функция считает сколько конфет взял и какой игрок и сколько осталось
# def p_print(name, k, counter, value):
#     print(
#         f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 1)  # флаг очередности (кто делает ход)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# # кто ходит последний тот и выиграл
# if flag :
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# вариант человек против бота:


# def input_dat(name):
#     x = int(
#         input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(
#         f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 1)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1, 29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
# if flag :
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# вариант человек против бота c "интеллектом":


def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# условие как ходит бот
def bot_calc(value):
    k = randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 1)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)
# кто ходит последний тот и выигрывает
if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
