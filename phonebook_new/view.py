
def show_menu():#основное меню
    print('Выберите необходимое меню!')
    print('Вы хотите: записать данные - 1;прочитать данные - 2;поиск абонента - 3;\n'
    'удаление абонента-4;корректировка данных - 5')
    return int(input('введите цифру: '))


def show_export():
    print('Выберите необходимое действие!')
    print('Вы хотите записать данные: вертикально  - 1; горизонтально  - 2')
    return int(input('введите цифру: '))


def show_import():#метод вывода данных
    print('Выберите необходимое действие!')
    print('вы хотите прочитать данные: данные в вертикальном формате - 1; данные в горизонтальном формате- 2')
    return int(input('введите цифру: '))


def get_info():  # метод ввода данных абонента
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info
    

def find():#метод поиска абонента
    print('По какому параметру ищем контакт: \n'
                '1 - Фамилия;\n'
                '2 - Имя;\n'
                '3 - номер телефона;\n')
                # '4 - описание;\n')
    a = int(input('Введите номер поиска: '))
    if a == 1:
        contact = input('Введите фамилию: ').title()
    if a == 2:
        contact = input('Введите имя: ').title()
    if a == 3:
        contact = input('Введите номер телефона: ')#.title()
    print('Будем искать по: ',contact)
    return contact


def delete():
    print('Введите индекс для удаления')
    return int(input())


def change_tel():
    print('Введите индекс для изменения через энтер')
    print('Введите новый телефон (11 цифр) через энтер')
    return int(input()), input()
