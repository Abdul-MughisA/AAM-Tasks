dict = {}

def fibRec(n):
    if n <= 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)
    #end if
#end def

def fibDyn(n):
    global dict
    if n <= 1:
        return n
    elif n in dict:
        return dict[n]
    else:
        dict[n] = fibDyn(n-1) + fibDyn(n-2)
        return fibDyn(n-1) + fibDyn(n-2)
    #end if

#end def

def fibIt(n):
    index = 2
    nums = [0, 1]
    for _ in range(n):
        nums.append(nums[index - 2] + nums[index - 1])
        index += 1
    #end for
    return nums[n]
#end def

print(fibDyn(32))
