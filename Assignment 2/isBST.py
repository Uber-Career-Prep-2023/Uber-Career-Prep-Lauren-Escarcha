# from BinarySearchTree import *

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree :
    def __init__(self):
        self.root = None

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
    
    # creates a new Node with data val in the appropriate location
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


class isBST:

    def __init__(self):
        self.root = None

    #when called, the root of a tree must be passed in
    def isBSTCheck(self, root):
        #do iteratively instead of recursion bc
        # if false, automatically stops
        stack = []

        cur = root
        prev_val = cur.val
        while(cur is not None and stack):
            
            while(cur):
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if cur.val < prev_val:
                return False
            
            cur = cur.right
    
        return True
    
def main():
    tree = BinarySearchTree()

    tree.insert(10) 
    tree.insert(8)
    tree.insert(16)
    tree.insert(9)
    tree.insert(13)
    tree.insert(17) 
    tree.insert(20) 
    tree.print()

    checkBST = isBST()
    print("\n---------\n" + str(checkBST.isBSTCheck(tree.root))) #true

main()
        
             


            
