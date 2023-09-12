#This program takes a number between 1 and 10 and then outputs the first 10 values of that number's times table.
num = int(input("Enter a number between 1 and 10: "))
#This loop prints the multiple.
for i in range(1, 11):
    print(i*num)
#end for