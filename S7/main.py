# переименовываем для кратности 
import controller as c
import logging as log

# если хотим, чтобы логи выводились в консоль
# logging.basicConfig(level=logging.INFO)

# если хотим, чтобы логи записывались в файл создает файл не в папке где остальные файлы
log.basicConfig(filename='log.txt',
                filemode='a', encoding="utf-8",
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=log.INFO)


# def main():
#     …
#     logging.info("Данные от пользователя получены")
#     …
#     logging.warning("Ошибка обработки данных")

c.run(log)






