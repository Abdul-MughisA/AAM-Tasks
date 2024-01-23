left = [2, 5, -1, -1, -1, -1]
name = ["John", "Peggy", "Alan", "Chris", "Sue", "Ken"]
right = [1, 4, 3, -1, -1, -1]

def traverse(pos):
    if left[pos] != -1:
        traverse(left[pos])
    #end if
    if right[pos] != -1:
        traverse(right[pos])
    #end if
    print(name[pos])
#end def
        
traverse(0)
