def FindEvenValues():
    numN = int(input("Введите число: "))

    if numN % 2 != 0:
        numN -= 1

    count = 0

    while count < numN:
        count += 2
        print(count)

FindEvenValues()