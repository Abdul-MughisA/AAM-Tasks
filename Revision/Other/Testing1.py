import time
startTime = time.time()

def fibonacci(n):
    if n == 0:
        return 0
    #end if
    if n == 1:
        return 1    
    #end if
    return fibonacci(n-1) + fibonacci(n-2)
#end def

def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
    # now append the sum of the two previous numbers to the list    
    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

test = 100

print(fibonacci(test))
time1 = time.time() - startTime
print(time1 * 1000, "milliseconds")

print(fibonacci2(test))
time2 = time.time() - startTime - time1
print(time2 * 1000, "milliseconds")