array = [7, 4, 6, 8, 1, 5]

def swap(a, b, array):
    temp = array[b]
    array[b] = array[a]
    array[a] = temp
#end def

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)
            #end if
        #end for
    #end for
#end def

print("Array to be sorted:", array)
bubbleSort(array)
print("Sorted array:", array)

# MAKE THE BUBBLE SORT STOP WHEN NO CHANGES ARE MADE ON A PASS #
# USUALLY THE BUBBLE SORT STOPS AFTER THE LENGTH OF THE ARRAY  #
