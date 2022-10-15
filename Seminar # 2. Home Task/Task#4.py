N = int(input("Введите число N: "))

def ShiftTwoPositionInRight():
    list = []
    for i in range(-N, N+1):
        list.append(i)
    print(list)

    steps = 2
    result = list[-steps:] + list[:-steps]
    print(result)

ShiftTwoPositionInRight()