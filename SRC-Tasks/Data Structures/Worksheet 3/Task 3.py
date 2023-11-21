class Node:
    def __init__(self, data, pointer) -> None:
        self.data = data
        self.pointer = pointer
    #end def

    def __repr__(self) -> str:
        return "Data: " + self.data + ", Pointer: " + str(self.pointer)
    #end def
#end class

myList = [Node("",-1) for _ in range(50)]
for index in range(49):
    myList[index].pointer = index + 1
#end for
myList[49].pointer = -1
start = -1 # The start of the list.
nextfree = 0 # The next free space in the list. Needs to be 0 because it's the first.

# start_pointer = 1
# next_free_pointer = 3
# def outputList(arr):
    # global start_pointer
    # current_pointer = start_pointer
    # while current_pointer != -1:
        # print(arr[current_pointer].data)
        # current_pointer = arr[current_pointer].pointer
    # end while
# end def

def AddItem(newName, myList):
    global nextfree
    global start
    if nextfree == -1: # Checks if there are no more free spaces in the list.
        print("ERROR!")
    else:
        myList[nextfree].data = newName # Places the new name into the next free space.
        if start == -1: # If the list is brand new,
            temp = myList[nextfree].pointer # Set a random variable temp to the the pointer of the next free item.
            myList[nextfree].pointer = -1 # Changes the pointer of the next free space to -1.
            start = nextfree # The start of the list is now the same as nextfree.
            nextfree = temp # nextfree is changed back to the pointer of the next free item.
        else: # But if the list isn't brand new,
            p = start # p is set to the same value as the start of the list.
            if newName < myList[p].data: # Checks if newName is less that what's at the start of the list.
                myList[nextfree].pointer = start # If it is less, then the pointer of the next free item leads back to the start of the list.
                start = nextfree # And the nextfree index becomes the same as the start of the list.
            else: # If the newName is greater than what is at the the start of the list.
                placeFound = False
                while myList[p].pointer != -1 and placeFound == False: # Loop only runs while the end of the list hasn't been reached (and placeFound == False).
                    if newName >= myList[myList[p].pointer].data: # Checks if newName is greater than the data in the next element in the list.
                        p = myList[p].pointer # P then becomes the pointer to the data element just checked (i.e.: the index).
                    else:
                        placeFound = True # Loop keeps running until newName is less than the data in the next element.
                    #end if (4)
                    temp = nextfree # temp holds the index of the next free space.
                    nextfree = myList[nextfree].pointer # nextfree then changes to be the pointer of the next free space.
                    myList[temp].pointer = myList[p].pointer # The pointer of the previous next free space = the pointer of ??
                    myList[p].pointer = temp # ??
                #end while
            #end if (3)
        #end if (2)
    #end if (1)

AddItem("A", myList)
print(myList)
AddItem("B", myList)
print(myList)
AddItem("C", myList)
print(myList)
# AddItem("Colin", myList)
# AddItem("Albert", myList)
# AddItem("Barry", myList)
# AddItem("Derek", myList)
# AddItem("Fred", myList)
# print(myList)
# AddItem("Trevor", myList)

# DEBUGGING:
# Albert goes missing after Barry is added.
# This probably means that some pointers are not being updated.
# Let's run through the code to see what happens.