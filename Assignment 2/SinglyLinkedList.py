class Node:
    #constructor
    def __init__(self, data=0, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self): 
        #define head of list
        self.head = None
    
    def insertAtFront(self, val):
        #if the list is empty
        if not self.head:
            self.head = Node(val)

        #if list has stuff in it
        else:
            new_node = Node(val)
            #insert in front
            new_node.next = self.head
            self.head = new_node

        return self.head
    
    def insertAtBack(self, val):
        #if the list is empty
        if not self.head:
            self.head = Node(val)
        else:
            #iterate thru until at tail
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)

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
            new_node.next = curr.next
            curr.next = new_node
    
    def deleteFront(self):
        if self.head:
            # temp node 
            curr = Node(0)
            # temp next points to 2nd node in array
            curr.next = self.head.next
            # head becomes pointer to node^
            self.head = curr.next
        return self.head
    
    def deleteBack(self):
        if self.head:
            curr = self.head
            prev = self.head

            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
    
    def deleteNode(self, loc):
        if loc >= self.length():
            return
        elif loc == 0: 
            self.deleteFront()
        elif loc == self.length() - 1:
            self.deleteBack()
        prev, curr = self.head, self.head
        count = 0
        while count != loc:
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
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
        
        prev = None
        while self.head.next:
            #basically flipping the pointers in other direction
            next = self.head.next 
            self.head.next = prev
            prev = self.head 
            self.head = next 
        self.head.next = prev
    
    def reverseRecursive(self):

        head = self.head

        return self.reverse(head, None)
    
    def reverse(self, cur, prev):
        if cur is None:
            # reinitialize the head!!!!!!
            self.head = prev
            return prev
        else:
            next = cur.next

            # reverses pointer
            cur.next = prev

            print("cur " + str(cur.data))

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
    list.print()
    
    list.reverseIterative() # 6 4 2
    list.print()

    list.reverseRecursive() # 2 4 6
    list.print()

main()
