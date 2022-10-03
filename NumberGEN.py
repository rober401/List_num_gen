def printValues():
    print("")
    x = input("How many number would you like: ")
    l = list()
    for i in range(1, int(x)):
        l.append(i ** 1)
    print(l)

printValues()