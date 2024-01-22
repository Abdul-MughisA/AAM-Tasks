import time

# ITERATIVE #
def fibIt(n):
    index = 2
    nums = [0, 1]
    for _ in range(n):
        nums.append(nums[index - 2] + nums[index - 1])
        index += 1
    #end for
    return nums[n]
#end def

# RECURSIVE #
def fibRec(n):
    if n <= 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)
    #end if
#end def

startTime = time.time()
print(fibIt(40))
time1 = time.time()
print(fibRec(40))
endTime = time.time()

itTime = time1 - startTime
recTime = endTime - time1

print("Iterative:", itTime, "seconds.")
print("Recursive:", recTime, "seconds.")
