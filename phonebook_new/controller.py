import view
import model


def run():#вывод  меню
    menu = view.show_menu()
    if menu == 1:
            data = view.get_info()#ввод данных нового абонента сразу в горизонтальном и вертикальном виде ,чтобы база данных для поиска была одна
            # res = view.show_export()#вывод меню для записи этих данных
            # if res == 1:
            model.txt_data_record(data)
            # elif res == 2:
            model.csv_data_record(data)
            run()

     

    elif menu == 2:  # вывод меню для дальнейших действий с
            res = view.show_import()  # вывод меню для чтения телефонной книги
            if res == 1:
               model.txt_data_reading()  # вертикальный вывод информации в терминал
            elif res == 2:
              model.csv_data_reading()  # горизонтальный вывод информации в терминал
            run()
    
    
    elif menu == 3:#поиск абонента
            print(' Ищем абонента ')
            contact = view.find()#ввод данных для поиска абонента
            model.reading_file(contact)#поиск абонента через метод поиска
            run()
   

    elif menu == 4:  # удаление абонента
            index = view.delete()
            model.del_info(index)
            run()
    
    elif menu == 5:#корректировка телефона
            index, tel = view.change_tel()
            model.update_info_new(index, tel)
            run()
        