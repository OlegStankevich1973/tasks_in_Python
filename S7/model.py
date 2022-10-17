def calc(text,log):
    # проверка на возникновении ошибки
    try:
    # функция eval выполняет строку-выражение, переданную ей в качестве обязательного 
    # аргумента и возвращает результат выполнения этой строки
        return eval(text)
    
    except SyntaxError:
        
            log.error(f'Синтаксическая ошибка')
            return'Неверная формула'
            
def convert(kg,log):
    try:
        return int(kg) * 1000
        # функция Exception ловит все ошибки
    except Exception:
            log.error(f'При конвертации {kg} в граммы возникла ошибка приведения к Int')
            return'Ошибка ввода'
