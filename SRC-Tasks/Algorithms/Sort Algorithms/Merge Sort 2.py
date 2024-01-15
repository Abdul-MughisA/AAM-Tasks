def merge(left, right):
    leftindex, rightindex, newindex = 0, 0, 0
    new = []
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            new.append(left[leftindex])
            leftindex += 1
        else:
            new.append(right[rightindex])
            rightindex += 1
        newindex += 1
        #end if
    new += left[leftindex:]
    new += right[rightindex:]
    #end while
    return new
#end def

def merge2(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    return merge(merge2(alist[:mid]), merge2(alist[mid:]))
     
#end def
#*********** MAIN PROGRAM ***************
alist = [3, 1, 9, 8, 4, 6]
print("Unsorted list:", alist)
print("Sorted list:", merge2(alist))
