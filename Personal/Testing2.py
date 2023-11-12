import random

loop1 = 0

list1 = [(random.randint(0, 3000)) for _ in range(500)]
list2 = [(random.randint(0, 3000)) for _ in range(500)]

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

list1.sort()
print(list1, "SORTED.")