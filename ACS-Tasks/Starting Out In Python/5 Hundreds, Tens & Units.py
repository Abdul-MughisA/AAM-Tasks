#This program asks for an integer between 100 and 999 and then displays the hundreds, tens and units.
integer = int(input("Enter an integer between 100 and 999: "))
hundreds = integer // 100
tens = (integer - (hundreds * 100)) // 10
units = integer - (hundreds * 100)
units = units - (tens * 10)
print("This number has", hundreds, "hundreds,", tens, "tens, and,", units, "units.")