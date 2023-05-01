class Node:
    #constructor
    def __init__(self, data=0, next=None, prev=None): 
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self): 
        #define head of list
        self.head = None
        #does a doubly linked list have a tail var? yes
        self.tail = None
    
    def insertAtFront(self, val):
        #if the list is empty
        if not self.head:
            self.head = self.tail = Node(val)
            
        #if list has stuff in it
        else:
            new_node = Node(val)
            #insert in front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        return self.head
    
    def insertAtBack(self, val):
        #if the list is empty
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            #iterate thru until at tail
            temp = self.head
            while temp.next:
                temp = temp.next

            #once reached end
            new_node = Node(val)
            #insert in back
            new_node.prev = temp
            temp.next = new_node
            self.tail = new_node

    def insertAfter(self, val, pos):
        #if position is invalid or head insertion is empty
        if pos >= self.length() or not self.head:
            return
        elif pos == self.length() - 1:
            #if insertion is at last position
            self.insertAtBack(val)
        else:
            curr = self.head
            count = 0
            while count != pos:
                curr = curr.next
                count += 1

            new_node = Node(val)
            curr.next.prev = new_node
            new_node.next = curr.next
            new_node.prev = curr
            curr.next = new_node            

    
    def deleteFront(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None

        return self.head
    
    def deleteBack(self):
        if self.head:
            curr = self.head
            before = self.head

            while curr.next:
                before = curr
                curr = curr.next

            #at last node
            before.next = None
            self.tail = before
    
    def deleteNode(self, loc):
        if loc >= self.length():
            return
        elif loc == 0: 
            self.deleteFront()
        elif loc == self.length() - 1:
            self.deleteBack()

        before, curr = self.head, self.head
        count = 0
        while count != loc:
            before = curr
            curr = curr.next
            count += 1

        before.next = curr.next
        curr.next.prev = before
        return self.head
    
    def length(self):
        if not self.head:
            return 0
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count

    def reverseIterative(self):
        if not self.head:
            return
        
        before = None
        self.tail = self.head
        while self.head.next:
            #basically flipping the pointers in other direction
            after = self.head.next 
            self.head.next = before
            self.head.prev = after

            before = self.head 
            self.head = after 

        self.head.next = before
        self.head.prev = None
    
    def reverseRecursive(self):

        head = self.head
        self.tail = self.head

        return self.reverse(head, None)
    
    def reverse(self, cur, prev):
        if cur is None:
            # reinitialize the head!!!!!!
            self.head = prev
            return prev
        else:
            next = cur.next

            # reverses pointer
            cur.prev = next
            cur.next = prev

            # print("cur " + str(cur.data))

            # if next is not None:
            #     print("prev " + str(next.data))
            # else: 
            #     print("prev " + str(next))

            return self.reverse(next, cur)
         
        
    # prints list
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    # prints list backwards
    def printBackwards(self):
        curr = self.tail

        while curr:
            print(curr.data, end=" ")
            curr = curr.prev
        print()

def main():
    list = LinkedList()

    list.insertAtFront(2)   # 2
    list.insertAtFront(1)   # 1 2
    list.insertAtBack(3)    # 1 2 3 
    list.insertAtBack(4)    # 1 2 3 4 
    list.insertAfter(5, 3)  # 1 2 3 4 5
    list.deleteFront()      # 2 3 4 5
    list.deleteBack()       # 2 3 4
    list.deleteNode(1)      # 2 4
    list.insertAtBack(6)    # 2 4 6
    print("starting from head: ")
    list.print()
    print("starting from tail: ")
    list.printBackwards()
    print("-----------")

    list.reverseIterative() # 6 4 2
    print("REVERSE ITER starting from head: ")
    list.print()
    print("REVERSE ITER starting from tail: ")
    list.printBackwards()
    print("-----------")

    list.reverseRecursive() # 2 4 6
    print("REVERSE RECUR starting from head: ")
    list.print()
    print("REVERSE RECUR starting from tail: ")
    list.printBackwards()

main()
