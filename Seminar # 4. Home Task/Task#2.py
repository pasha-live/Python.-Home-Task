def OpenFile(name):
    data = open(name, encoding='utf-8')
    iceCream = data.read()
    data.close()
    iceCream = iceCream.split(', ')
    return iceCream

allIceCream = OpenFile('assortment.txt')
iceCreamInSklad = OpenFile('assortmentInSklad.txt')

result = list(set(allIceCream) ^ set(iceCreamInSklad))
print(result)