def GetCoordQuarter():
    num = int(input("Введите номер четверти: "))

    if num < 1 or num > 4:
        print("Неверный номер четверти")

    match num:
        case 1:
            print(f"В первой четверти X > 0, Y > 0"),
        case 2:
            print(f"В второй четверти X > 0, Y < 0"),
        case 3:
            print(f"В третьей четверти X < 0, Y < 0"),
        case 4:
            print(f"В четвёртой четверти X < 0, Y > 0"),

GetCoordQuarter()
