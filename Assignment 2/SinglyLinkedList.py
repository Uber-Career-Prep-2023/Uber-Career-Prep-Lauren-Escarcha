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
            self.head = new_node.next

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

    def insertAfter(self, val, i):
        if i == self.length() or not self.head:
            return
        elif i == self.length() - 1:
            self.insertAtBack(val)
        else:
            curr = self.head
            count = 0
            while count != i:
                curr = curr.next
                count += 1
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
    
    # removes first Node; returns new head
    def deleteFront(self):
        if self.head:
            dummy = Node(0)
            dummy.next = self.head.next
            self.head = dummy.next
        return self.head.val
    
    # removes last Node
    def deleteBack(self):
        if self.head:
            curr = self.head
            prev = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
    
    # removes node at index; returns head
    def deleteNode(self, i):
        if i == self.length():
            return
        elif i == 0: 
            self.deleteFront()
        elif i == self.length() - 1:
            self.deleteBack()
        prev, curr = self.head, self.head
        count = 0
        while count != i:
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
    
    # returns length of linked list
    def length(self):
        if not self.head:
            return 0
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count

    # reverses Linked List iteratively
    def reverseIterative(self, head):
        if not self.head:
            return
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
    # reverses Linked List recursively
    def reverseRecursive(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead
        
    # prints list
    def print(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        print('| ', end="")
        for i in res: 
            print(i, end = " | ")

def main():
    list = LinkedList()

    list.insertAtFront(1)  
    list.insertAtFront(2)  
    list.insertAtBack(3)   
    list.insertAtBack(4)   
    list.insertAtBack(5)   
    list.deleteFront()    
    list.deleteBack()    
    list.deleteNode(1)   
    
    list.print()

main()
