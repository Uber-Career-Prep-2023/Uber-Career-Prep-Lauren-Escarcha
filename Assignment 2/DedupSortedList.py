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
    

    #could use deleteNode func from Linked List class,
    # but made new method solely for this    
    def removeDuplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                #remove duplicate
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return
    
    # prints list
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        return

def main():
    list = LinkedList()

    list.insertAtBack(1)   # 2
    list.insertAtBack(1)   # 1 1
    list.insertAtBack(2)   # 1 1 2
    list.insertAtBack(3)   # 1 1 3
    list.insertAtBack(4)   # 1 1 3 4
    list.insertAtBack(4)   # 1 1 3 4 4
    list.insertAtBack(4)   # 1 1 3 4 4 4
    list.insertAtBack(4)   # 1 1 3 4 4 4 4
    list.print()

    list.removeDuplicates()
    print()
    list.print() # 1 2 3 4 


main()
