# 	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные	Выходные данные
# 3
# Hello Hi
# Bye Goodbye           Bye
# List Array
# Goodbye
 
	              
vocab = {}
text = open ('4-5.txt','r') 
for line in text: 
        a = line.split()
        print(a)
        if len(a) == 2: 
            vocab[a[0]] = a[1] 
        if len(a) == 1: 
            word = a[0] 
text.close() 
print (f"Ищем синоним для слова: {word}") 
for k, v in vocab.items():  
    if v == word: 
        print(k) 
    if k == word: 
        print(v) 

