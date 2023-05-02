from collections import deque

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
    
    def LeftView(self):
        return self.LeftViewHelper(self.root)

    def LeftViewHelper(self, cur):
        res = []
        q = deque([cur])

        while q:
            leftSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    leftSide = node
                    #left child before right
                    q.append(node.left)
                    q.append(node.right)
            if leftSide:
                res.append(leftSide.val)
        return res
                

def main():
    bst = BinarySearchTree()

    # used https://www.cs.usfca.edu/~galles/visualization/BST.html
    # to visualize tree
    bst.insert(7) 
    bst.insert(8)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(9)
    bst.print()

    #should be 7 8 9 5 6
    res = bst.LeftView()
    print()

    for i in range(len(res)):
        print(res[i])
    

main()