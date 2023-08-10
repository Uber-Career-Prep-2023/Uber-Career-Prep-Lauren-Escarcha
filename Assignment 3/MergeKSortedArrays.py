import heapq

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    #edge case: if no lists
    if not lists or len(lists) == 0:
        return None

    #merge lists, two by two until only 1 left
    while len(lists) > 1:

        updatedMerges = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]

            if (i+1) < len(lists):
                l2 = lists[i+1]
            else:
                l2 = None

            updatedMerges.append(self.mergeLists(l1, l2))

        lists = updatedMerges

    return lists[0]

def mergeLists(self, l1, l2):  
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next