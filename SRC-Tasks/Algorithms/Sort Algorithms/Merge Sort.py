alist = [1, 3, 4, 6, 8, 9]
blist = [2, 5, 12, 14, 17]
clist = [0 for _ in range(len(alist)+len(blist))]
done = False
i = 0

def merge(left, right, new):
    global i
    leftindex, rightindex, newindex = 0, 0, 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            new[newindex] = left[leftindex]
            leftindex += 1
        else:
            new[newindex] = right[rightindex]
            rightindex += 1
        newindex += 1
        #end if
        while leftindex < len(left):
            new[newindex] = left[leftindex]
            leftindex += 1
            newindex += 1
        #end while
        while rightindex < len(right):
            new[newindex] = right[rightindex]
            rightindex += 1
            newindex += 1
        #end while
    #end while
#end def

print(clist)
merge(alist, blist, clist)
print(clist)
