# minimum = int(input(" Please Enter the Minimum Value : ")) 
# Oddtotal = 0
# for number in range(minimum):
#     if number % 2 != 0:
#         print(number)
#         Oddtotal = Oddtotal + number
# print("The Sum of Odd Numbers from",Oddtotal)


no = int(input(" Please Enter the Value : ")) 
i = 0
sum=0
while i <= no:
    if i% 2 != 0:
        print(i)
        sum+=i
    i+=1
print("The Sum of Odd Numbers here...",sum)
    
