def show_menu():
    print('Выберите необходимое меню!')
    print('вы хотите: записать данные - 1; прочитать данные - 2')
    return int(input('введите цифру: '))


def show_export():
    print('Выберите необходимое действие!')
    print('вы хотите записать данные: файл txt - 1; файл csv - 2')
    return int(input('введите цифру: '))


def show_import():
    print('Выберите необходимое действие!')
    print('вы хотите прочитать данные: файл txt - 1; файл csv - 2')
    return int(input('введите цифру: '))



def get_info():#метод ввода данных
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
