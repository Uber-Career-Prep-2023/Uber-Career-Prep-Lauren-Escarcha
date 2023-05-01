class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree :

    def __init__(self):
        self.root = None

    #wanted to do insertion recursively, 
    #but followed the params of the functions outlined
    def insertHelper(self, cur, val):

        newNode = Node(val)

        if cur is None:
            return Node(val) 
        else:
            #less than, move to left
            if cur.val > val:
                cur.left = self.insertHelper(cur.left, val)
            #more than, move to right
            elif cur.val < val:
                cur.right = self.insertHelper(cur.right, val)

            #if equal to val, already added
            return cur

    # creates a new Node with val val in the appropriate location
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        self.insertHelper(self.root, val)
    
    #for testing
    def inorder(self, cur):
        if cur is None:
            return
        
        self.inorder(cur.left)
        print(cur.val, end=" ")
        self.inorder(cur.right)

    #actually print 
    def print(self):
        cur = self.root
        return self.inorder(cur)
    
    def FloorInBST(self, val):
        cur = self.root
        if self.root:
            floor = self.root.val
        while cur:
            if cur.val == val:
                return val
            if cur.val < val:
                floor = cur.val
                cur = cur.right
            else:
                cur = cur.left
        return floor

def main():
    bst = BinarySearchTree()

    bst.insert(10) 
    bst.insert(8)
    bst.insert(16)
    bst.insert(17)
    bst.insert(13)
    bst.insert(9) 
    bst.insert(20)

    bst.print()
    print()
    print(bst.FloorInBST(13))
    print(bst.FloorInBST(15))

main()