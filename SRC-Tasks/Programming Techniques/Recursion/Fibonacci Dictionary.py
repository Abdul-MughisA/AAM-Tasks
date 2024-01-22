def fib(n):
    if n in fib_dict:
            return fib_dict[n]
    else:
        if n <= 1:
            fib_dict[n] = 1
            return 1
        else:
            fib_dict[n] = fib(n-1) + fib(n-2)
            return fib_dict[n]
        #end if
    #end if
#end def


fib_dict={}
print (fib(12))
