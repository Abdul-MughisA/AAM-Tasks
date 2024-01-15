class Stack():
    def __init__(self, size) -> None:
        self.maxSize = size
        self.data = ["" for _ in range(size)]
        self.sp = -1
    #end def

    def size(self):
        return self.sp + 1
    #end def

    def isFull(self):
        return self.size() == self.maxSize
    #end def

    def isEmpty(self):
        return self.sp == -1
    #end def

    def push(self, item):
        if self.isFull():
            print("Is Full!")
        else:
            self.sp += 1
            self.data[self.sp] = item
        #end if
    #end def

    def pop(self):
        if self.isEmpty():
            print("Is Empty!")
        else:
            self.sp -= 1
            return self.data[self.sp + 1]
    #end def

    def peek(self):
        while not self.isEmpty():
            return self.data(self.sp)
        #end while
    #end def
#end class



myString = input("Please enter a word or phrase to be tested: ")
numChars = len(myString)
s = Stack(numChars)
palList = []

for c in myString:
    s.push(c)
    print(s.data)
#end for

while not s.isEmpty():
    palList.append(s.pop())

palString = "".join(palList)

if palString == myString:
    print("This is a palindrome.")
else:
    print("This is not a palindrome; an error occurred.")