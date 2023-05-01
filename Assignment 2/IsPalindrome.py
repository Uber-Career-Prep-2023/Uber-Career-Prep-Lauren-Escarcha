import math

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
    
    def length(self):
        if not self.head:
            return 0
        curr = self.head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        return count

    # prints list
    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def isPalindrome(self):
        length = math.floor(self.length())

        #nothing = no palindrome
        if self.head is None:
            return False

        frontInd = 0
        backInd = length-1
        front = self.head
        back = self.tail

        while frontInd <= backInd:
            if front.data != back.data:
                return False
            front = front.next
            back = back.prev
            frontInd +=1
            backInd -=1

        return True



def main():
    list = LinkedList()

    list.insertAtFront(9)   # 9
    list.print()
    print("= " + str(list.isPalindrome()))

    list.insertAtFront(2)   # 9 2
    list.insertAtFront(4)   # 9 2 4
    list.insertAtFront(2)   # 9 2 4 2
    list.insertAtFront(9)   # 9 2 4 2 9

    list.print()
    print("= " + str(list.isPalindrome()))

    list.insertAtFront(0)   # 9 2 4 2 9

    list.print()
    print("= " + str(list.isPalindrome()))

main()
