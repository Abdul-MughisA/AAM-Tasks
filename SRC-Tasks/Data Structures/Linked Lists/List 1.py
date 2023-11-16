class Node:
    def __init__(self, data, pointer) -> None:
        self.data = data
        self.pointer = pointer
    #end def

    def __repr__(self) -> str:
        return "Data: " + self.data + ", Pointer: " + str(self.pointer)
    #end def
#end class

linkedListData = []
linkedListData.append(Node("Lucas", 2))
linkedListData.append(Node("A'yaan", 0))
linkedListData.append(Node("Suren", -1))
linkedListData.append(Node("Empty", 4))
linkedListData.append(Node("Empty", -1))

startPointer = 1
nextFreePointer = 3

print(linkedListData)