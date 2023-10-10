# This code assumes that printing an array will print the array in a nice format automatically.

park = [["empty" for _ in range(1, 11)] for __ in range(1, 7)]
reg = input("Enter reg number: ")
row = int(input("Enter row: "))
column = int(input("Enter column/space: "))
if park[row][column] == "empty":
    park[row][column] = reg
else:
    print("Space is taken, please re-enter.")
print(park)