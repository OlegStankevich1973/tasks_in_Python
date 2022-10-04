# 	В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
# сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# Входные данные	      Выходные данные
# one two one tho three	    0 0 1 0 0
string = 'one two one tho three one one tho tho one'
list = []
list = string.split(' ')
print (list)
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
        print(dict[i], end=' ')
    else:
        dict[i] = 0
        print(dict[i], end=' ')
