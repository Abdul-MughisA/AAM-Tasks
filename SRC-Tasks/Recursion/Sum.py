numbers = [3, 6, 2, 8, 1]

def sum(list, length):
    if length == 0:
        total = list[length]
    else:
        total = list[length] + sum(list, (length - 1))
    #end if
    return total
#end def

print(sum(numbers, len(numbers) - 1))
