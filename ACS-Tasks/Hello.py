print("Hello, world!")

sunshine = 0
maxHours = 0
minHours = 100
totalSunshine = 0

sunshine = int(input("Input hours of sunshine: "))
if sunshine > maxHours:
	maxHours = sunshine
if sunshine < minHours:
	minHours = sunshine
totalSunshine =  totalSunshine + sunshine

print("Max sunshine hours: ", maxHours)
print("Min sunshine hours: ", minHours)
print("Total sunshine hours: ", totalSunshine)
