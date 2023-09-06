#This program asks the user for an integer and a diviser, and, using the MOD function, outputs the integer and the remainder.
integer = int(input("Enter an integer: "))
div = int(input("Enter a divisor: "))
int_ans = integer // div
remainder = integer% div
print("The answer is", int_ans, "remainder", str(remainder) + ".")