import math

def GetDistanceOfPoint():
    x1 = float(input("Введите координату точки x1: "))
    y1 = float(input("Введите координату точки x2: "))
    x2 = float(input("Введите координату точки y1: "))
    y2 = float(input("Введите координату точки y2: "))

    tmp = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    result = math.sqrt(tmp)
    print(result)

GetDistanceOfPoint()