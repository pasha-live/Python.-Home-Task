dictionaly = {
    'привет': 'Приветствую!',
    'как тебя зовут': 'меня зовут бот',
    'пока': 'До свидания!',
}

question = str(input("Задайте вопрос: "))

if question == 'привет':
    print(dictionaly['привет'])
if question == 'пока':
    print(dictionaly['пока'])
if question == 'как тебя зовут':
    print(dictionaly['как тебя зовут'])
if question not in dictionaly:
    print('я ещё не понимаю этого')