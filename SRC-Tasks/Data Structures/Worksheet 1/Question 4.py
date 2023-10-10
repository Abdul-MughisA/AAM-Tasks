# Same as question 3 but with more outlets.

# outletSales = 

total = [0 for _ in range(3)]
for quarter in range(3):
    for outlet in range(49):
        total[quarter] = total[quarter]  + outletSales[quarter,outlet]
    print(total[quarter])
