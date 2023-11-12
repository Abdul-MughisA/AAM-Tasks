loop1 = 0

list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]

list1.sort()
list2.sort()
for loop2 in range(len(list2)-1, -1, -1):
    moveNum = list2[loop2]
    loop = True
    while loop:
        loop1 += 1
        refNum = list1[loop1]
        if moveNum < refNum:
            list1.insert(loop1, list2.pop(loop2))
            loop1 = 0
            loop = False
        #end if
    #end while
#end for

print(list1)