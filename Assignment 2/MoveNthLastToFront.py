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
    
    def MoveNthLastToFront(self, n):
        dummy = Node(0)
        dummy.next = self.head

        # 2 pointer
        left = dummy
        right = self.head

        # make the gap, w left being node before nth
        while right and n > 0:
            right = right.next
            n -=1

        # find nth from last
        while right:
            right = right.next
            left = left.next

        # move left.next to front
        # transfer data, not location
        dummy.data = left.next.data
        self.head = dummy

        # delete nth from last element
        left.next = left.next.next

        return self.head       

    
    # prints list
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

def main():
    list = LinkedList()

    list.insertAtFront(15)
    list.insertAtFront(2)
    list.insertAtFront(8)
    list.insertAtFront(7)
    list.insertAtFront(20)
    list.insertAtFront(9)
    list.insertAtFront(11)
    list.insertAtFront(6)
    list.insertAtFront(19)  
    list.print()
    
    print("move 2nd from last:")
    list.MoveNthLastToFront(2) 
    list.print()

    print("move 7th from last:")
    list.MoveNthLastToFront(7) 
    list.print()

main()
