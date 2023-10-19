# INITIALISATIONS

MAX_SIZE = 5
q1 = [0 for _ in range(MAX_SIZE)]
q1_size = 0
q1_fp = 0
q1_rp = -1

# DEFINITIONS

def Empty():
    global q1_size
    return q1_size == 0
#end def

def Full():
    global MAX_SIZE
    global q1_size
    return MAX_SIZE == q1_size
#end def

def NQ(item):
    if not Full():
        q1_rp = (q1_rp + 1) % MAX_SIZE
        q1_size += 1
        q1[q1_rp] = item
    #end if
#end def

def DQ():
    if not Empty():
        item_p = q1_fp
        q1_fp = (q1_fp + 1) % MAX_SIZE
        q1_size -= 1
        return q1[item_p]
    #end if
#end def

NQ(1)
NQ(2)
NQ(3)
NQ(4)
NQ(5)