# метод показа меню
def show_menu():
    print ('1- Калькулятор')
    print('2 - Конвертер')
    return input('Введите цифру: ')

def show_calc_enter():
    return input('Введите выражение: ')

def show_calc_result(res):
    # str(res) потому что вводим через терминол строчные значения
    print('Результат вычисления = ' + str(res))

def show_converter_enter():
    return input('Введите количество  кг: ')

def show_convert_result(res):
    # res[0]это 0 значение из массива view.show_convert_result([kg,res]),те кг
    print(f'{res[0]} кг = {res[1]} г')