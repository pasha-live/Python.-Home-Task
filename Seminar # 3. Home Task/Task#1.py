N = int(input('Введите число N: '))

def GetValueFibonnachi(n):
    fib1 = fib2 = 1
    value = ['1\n', '1\n']
    for i in range(2, N):
        fib1, fib2 = fib2, fib1 + fib2
        value.append(f'{fib2}\n')
    return value

print(GetValueFibonnachi(N))

data = open("ValueFib.txt", 'w')
data.writelines(GetValueFibonnachi(N))
data.close()