import math

# Variables
num = 0
x = 1
y = 1
a = 2
b = 3

for num in range(100):
    x = 3 * x + 4 * y
    y = a * x + b * y
    print(x)
#end for