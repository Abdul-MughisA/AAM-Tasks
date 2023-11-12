class Node:
    def __init__(self, data, pointer) -> None:
        self.data = data
        self.pointer = pointer
    #end def

    def __repr__(self) -> str:
        return "Data:", self.data, "Pointer:", self.pointer
    #end def
#end class

linkedListData = []
linkedListData.append(Node("Empty", 1))
linkedListData.append(Node("Empty", 2))
linkedListData.append(Node("Empty", 3))
linkedListData.append(Node("Empty", 4))
linkedListData.append(Node("Empty", -1))

startPointer = -1
nextFreePointer = 0

print(linkedListData)