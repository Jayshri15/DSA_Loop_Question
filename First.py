num = int(input("enter the no..."))
i = 0
while i<=num:
    j = num
    while j >= i:
        print("*",end="")
        j = j - 1
    print()
    i = i + 1