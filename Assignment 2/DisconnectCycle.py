class Node:
    #constructor
    def __init__(self, data=0, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self): 
        #define head of list
        self.head = None
    
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
    
    def length(self):
        if not self.head:
            return 0
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count
    
    #inserts new node at end, and .next points to existing pos,
    #creating a cycle
    def insertCycleAt(self, val, pos):
        #find pos to return cycle to
        if pos >= self.length() or not self.head:
            return
        else:
            returnTo = self.head
            count = 0
            while count != pos:
                returnTo = returnTo.next
                count += 1

        #insert new node at BACK
        #iterate thru until at tail
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

        #make last node .next point to pos
        temp.next.next = returnTo

        return self.head
    
    def disconnectCycle(self):
        
        # don't think I can use tortoise and hare pointer?
        # bc does not guaruntee it finds the node where the cycle starts
        # so, I used a set to store node values
        # to find the exact node to break the cycle
        nodes = []

        if self.head is None:
            return
        
        # curr = where the cycle RETURNS to
        curr = self.head
        # prev = where the cycle STARTS 
        prev = None 
        while curr:
            if curr in nodes:
                #break cycle
                prev.next = None
                break
            else:
                nodes.append(curr)
                prev = curr
                curr = curr.next

        return self.head

    
    # prints list = SHOULD BE INFINITE LOOP
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

def main():
    list = LinkedList()

    list.insertAtBack(15)
    list.insertAtBack(2)
    list.insertAtBack(8)
    list.insertAtBack(7)
    list.insertAtBack(20)
    list.insertAtBack(9)
    list.insertAtBack(11)
    list.insertAtBack(6)
    # inserts node w data = 4,
    # and cycle to return to pos 4
    list.insertCycleAt(4, 4) 

    # test for INITIAL LL CYCLE
    # INFINITE LOOP
    # list.print()

    list.disconnectCycle()
    list.print()

    

main()
