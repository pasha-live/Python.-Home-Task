def truthTable():
    print("Таблица истинности для: ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"({x}, {y}) | {z} | {bool(not (x and y) or z)}")

truthTable()