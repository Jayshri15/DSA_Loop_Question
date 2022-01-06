N = int(input("enter the no___"))
row = 1
while row < N:
    var1 = 1
    var2 = row + var1
    while var2 > 1:
        print("*",end="")
        var2 = var2 - 1
    row = row + 1
    print()
    