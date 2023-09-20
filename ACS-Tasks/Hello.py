# This program prints "Hello, World!".
print("Hello, world!")

year = int(input("Enter a year: "))
LeapYear = False
if year % 4 == 0:
	LeapYear = True
elif year % 100 == 0:
	LeapYear = False

if year % 400 == 0:
	LeapYear = True

if LeapYear == True:
	print(year, "is a leap year.")

if LeapYear == False:
	print(year, "is not a leap year.")
