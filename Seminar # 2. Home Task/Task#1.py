N = int(input("Введите число N: "))

def FactorialN():
    fact = []
    count = 1
    for i in range(N):
        count += count * i
        fact.append(count)
    print(fact)

FactorialN()