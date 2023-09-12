#This program takes in 2 numbers and outputs them in numberical order with the highest first.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
#Checks which number is bigger.
if num1 < num2:
    print(num2, num1)
elif num2 < num1:
    print(num1, num2)
else:
    print("Something went wrong.")
#end if