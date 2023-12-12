def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList)-1
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if aList[midpoint] == itemSought:
            found = True
                                (3)
        else:
            if aList[midpoint] < itemSought:
                first = 
                pass
            else:	
                
            #end if
        #end if
    #end while
    return index		
#end def
