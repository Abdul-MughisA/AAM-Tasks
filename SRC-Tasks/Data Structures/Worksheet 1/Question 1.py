# Read 6 numbers into an array

print("Follow the progress of the program to find the total and mean of 6 numbers.")
print()

total = 0

num = [0 for _ in range(6)]
for i in range(0, 6):
    num[i] = int(input("Enter number: "))
    total += num[i]
#next i

print()
print("Your numbers in reverse are: ")
for j in range(5, -1, -1):
    print(num[j])
#next j

print()
print("The sum of your number is", str(total) + ".")

mean = total / 6

print()
print("The mean of your numbers is", str(mean) + ".")