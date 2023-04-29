class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree :

    def __init__(self):
        self.root = None

    #recursive func for min
    def minHelper(self, cur):
        min = cur.val

        while (min >= cur.val and cur.left):
            if(cur.val < min):
                min = cur.val
            cur = cur.left
        
        return cur.val


    #returns the minimum value in the BST = leftmost val
    def min(self):
        if self.root is None:
            return
        return self.minHelper(self.root)

    # returns the maximum value in the BST
    def max(self):
        if self.root is None:
            return

        #could use recursion but did a while loop instead
        max = self.root.val
        cur = self.root

        while (max <= cur.val and cur.right):
            if(cur.val < max):
                max = cur.val
            cur = cur.right
        
        return cur.val
        
    #returns a boolean indicating whether val is present in the BST
    def contains(self, val):
        cur = self.root

        while(cur and cur.val != val):
            if(cur.val < val):
                cur = cur.right
            elif(cur.val > val):
                cur = cur.left
        if(cur):
            return True
        return False

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

    
    # creates a new Node with data val in the appropriate location
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        self.insertHelper(self.root, val)

    #helper function for deletion recursion
    def deleteHelper(self, cur, val):
        if cur is None:
            return cur
        elif(val < cur.val):
            self.deleteHelper(cur.left, val)
        elif(val > cur.val):
            self.deleteHelper(cur.right, val)
        #the meat
        else:
            print(cur.val)
            #if node has ONE or no child
            if cur.left is None:
                temp = cur.right
                cur = None
                return temp
            elif cur.right is None:
                temp = cur.left
                cur = None
                return temp
            
            #TWO children 
            # get smallet in right subtree
            temp = self.minHelper(cur.right)

            # copy temp val into cur
            cur.val = temp.val

            #delete 
            cur.right = self.deleteHelper(cur.right, temp.val)

        return cur
            


    #deletes the Node with data val, if it exists
    def delete(self, val):
        print(self.deleteHelper(self.root, val).val)
        return 
    
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

def main():
    bst = BinarySearchTree()

    bst.insert(1) 
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(5) #should not have duplicates

    #initial tree test
    bst.print()

    #min and max test
    print("\nmin: " + str(bst.min()))
    print("max: " + str(bst.max()))

    #contains = true
    print("contains 3: " + str(bst.contains(3)))
    #contains = false
    print("contains 9: " + str(bst.contains(9)))

    #delete 
    bst.delete(5)
    # tree test
    bst.print()

main()