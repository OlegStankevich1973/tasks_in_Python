# Дан список, вывести отдельно буквы и цифры.
# a = (‘1’, 'a', 'b', '2', '3', 'c')
# b = ('a', 'b', 'c')
# c = ('1', '2', '3')
lst = ['1','vd','we','3','*']
print(lst)
# i.isdigit() функция передает true если в списке цифры(т е выводит цифры)
print([i for i in lst if not i.isdigit()])#так выводит буквы с символами
print([i for i in lst if  i.isdigit()])
# i.isalpha() функция передает true если в списке ,буквы(т е выводит только буквы)
print([i for i in lst if  i.isalpha()])
