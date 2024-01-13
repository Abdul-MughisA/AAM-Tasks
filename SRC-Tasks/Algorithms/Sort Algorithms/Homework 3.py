import time

n = 4
aList = [7, 3, 6, 2]

for i in range(1, n):
    currentvalue = aList[i]

    pointer = i - 1

    while pointer >= 0 and aList[pointer] > currentvalue:

        aList[pointer + 1] = aList[pointer]

        pointer = pointer - 1

    #end while
    aList[pointer + 1] = currentvalue

#end for

print(aList)
