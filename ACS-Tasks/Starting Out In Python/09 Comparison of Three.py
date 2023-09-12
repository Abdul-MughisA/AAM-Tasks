#This program takes 3 integers and outputs then in numerical order with the highest first.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter yet another number: "))

#Checks which number is bigger using all combinations.
if num1 < num2 and num2 < num3:
    print(num3, num2, num1)
elif num3 < num2 and num2 < num1:
    print(num1, num2, num3)
elif num2 < num3 and num3 < num1:
    print(num1, num3, num2)
elif num1 < num3 and num3 < num2:
    print(num2, num3, num1)
elif num2 < num1 and num1 < num3:
    print(num3, num1, num2)
elif num3 < num1 and num1 < num2:
    print(num2, num1, num3)
else:
    print("Something went wrong.")
#end if