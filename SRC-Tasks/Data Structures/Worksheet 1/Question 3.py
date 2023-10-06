# Calculates sales for the quarter.

outlet1sales = [10, 12, 15, 10]
outlet2sales = [5, 8, 3, 6]
outlet3sales = [10, 12, 15, 10]

total = 0

for i in range(4):
    total = outlet1sales[i] + outlet2sales[i] + outlet3sales[i]
    print("Total for quarter", str(i + 1) + str(": ") + str(total))
#end for