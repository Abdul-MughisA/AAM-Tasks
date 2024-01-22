def sumEven(n):
    if n > 0 and n % 2 == 0:
        return n + sumEven(n - 2)
    else:
        return 0
    #end if
#end def

print(sumEven(6))

def addNums(numbers):
    if len(numbers) > 1:
        numbers[0] = numbers[0] + addNums(numbers[1:])
    #end if
        
    print(numbers[0])
    return numbers[0]
#end def

marks = [3,6,2,8]
total = addNums(marks)
print("Total =", total)
