#This program outputs the factors of a given number.
originalNumber = int(input("Enter a number to find the factors for: "))
print("Factors: ")

#for loop to check each number between 2 and the actual number.
for i in range(2, originalNumber):

    #if statement to check if the number is fully divisible.
    if originalNumber % i == 0:
            print(i)
    #end if
#end for