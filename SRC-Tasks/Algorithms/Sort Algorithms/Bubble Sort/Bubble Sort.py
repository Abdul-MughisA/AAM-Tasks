array = [7, 4, 6, 8, 1, 5]

def swap(a, b, array):
    temp = array[b]
    array[b] = array[a]
    array[a] = temp
#end def

print(array)
swap(0, 1, array)

# MAKE THE BUBBLE SORT STOP WHEN NO CHANGES ARE MADE ON A PASS #
# USUALLY THE BUBBLE SORT STOPS AFTER THE LENGTH OF THE ARRAY  #
