str1 = "one"
str2 = "onetwonineeeeee"

def GetEntrySymbol():
    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        print(f"Кол-во вхождений {str1[i]}: {count} раз")

GetEntrySymbol()