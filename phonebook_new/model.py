import csv

import view #import get_info as gi
#info = gi


def csv_data_open():      # открытие файла csv и переформатирование в list
    with open("phonebook_new/csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        file_csv = list(file_csv)
    return file_csv


def csv_data_record(info):  # запись файла csv
    with open("phonebook_new/csv_data.csv", 'a', encoding='utf-8', newline='') as r_file:  # открываем файл
        file_csv = csv.writer(r_file, delimiter=";",
                              lineterminator="\n")  # создаем писателя
        # с помощью писателя записываем данные в файл
        file_csv.writerow([info[0], info[1], info[2], info[3]])
        # r_file.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')#или так можно без 10 и 11
    return file_csv


def txt_data_record(info):     # запись файла txt
    with open("phonebook_new/txt_data.txt", "a", encoding='utf-8') as file:
        file.write(
            f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
    return file.write


def txt_data_reading():     # чтение файла txt
    with open("phonebook_new/txt_data.txt", "r", encoding='utf-8') as file:
        file_txt = file.read()
        print(file_txt)
    return file_txt


def csv_data_reading():  # чтение данных файла csv
    with open('phonebook_new/csv_data.csv', 'r', encoding='utf-8') as r_file:
        csv_open = csv.reader(r_file, delimiter=';')
        for row in csv_open:
            print(','.join(row))


def reading_file(param):#чтение файла
    b = view.data_output()
    if b == 1:
        with open('phonebook_new/csv_data.csv', 'r',encoding='utf-8') as file:
            for line in file:
                if param in line:
                    print (line)
    if b == 2:
        # list_csv = csv_data_open()
        with open('phonebook_new/csv_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            # print (list(reader))
            for line in reader:
                print(line)
                # if param in line:
                #     list = line.split(';')
                #     print(list)
                    # print(f'{list[0]}\n,{list[1]}\n,{list[2]}\n,{list[3]}\n')

