N = int(input('Введите число для разделителя на простые множители: '))

def GetMult(n):
    Multiplier = []
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            Multiplier.append(divider)
            n //= divider
        else:
            divider += 1
    if n > 1:
        Multiplier.append(n)
    return Multiplier

print(f'Делители числа {N}: {GetMult(N)}')