class TreeNode():
    def __init__(self, value, left = -1, right = -1) -> None:
        self.left = left
        self.right = right
        self.value = value
    #end def
#end class

treeList = []

def insertTreeNode(treeList, value):
    newNode = TreeNode(value)
    if len(treeList) == 0: # ROOT #
        treeList[0] = newNode
    else:
        current = 0
        next = 0
        while next != -1:
            if value < treeList[current].value:
                current = treeList[current].left
                next = treeList[current].left
            #end if
        #end while
    #end if
#end def
