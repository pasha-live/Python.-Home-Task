data = open('fruct.txt', encoding='utf-8')
text = data.read()
data.close()
text = text.split()

symbol = input('Введите первую букву фрукта (заглавную): ')

for value in text:
    if value[0] == symbol:
        print(value, end=' ')