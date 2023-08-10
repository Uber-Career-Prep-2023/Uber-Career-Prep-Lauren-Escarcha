import math

class PriorityQueue:
    
    def __init__(self):
        #array of pairs (string, int)
        self.maxHeap = []

    def top(self):
        return self.maxHeap[0]

    def insert(self, pair):
        #1 - add element to end (rightmost of last level)
        self.maxHeap.append(pair)

        #index of inserted num and given parents
        child = len(self.maxHeap) - 1
        parent = math.floor((child-1)/2)

        #HEAPIFY UP:
        #while not root
        #and parent is LESS than child
        while(child > 0 and self.maxHeap[int(parent)][1] > self.maxHeap[child][1]):
            #swap 

            self.maxHeap[(parent)], self.maxHeap[child] = self.maxHeap[child], self.maxHeap[(parent)]
            child = parent
            parent = math.floor((child-1)/2)

    def delete(self):
        #edge case
        if self.maxHeap is None or len(self.maxHeap) == 0:
            return

        #1 - move last element to root (and delete og root value)
        self.maxHeap[0] = self.maxHeap[len(self.maxHeap)-1]

        #2 - delete the last index, decrease size
        self.maxHeap.pop()

        #3 - heapify to maintain order
        self.heapify(0)


    #build heap from array = start from back of array
    #delete node in heap = start from beginning of array
    def heapify(self, i):

        left = 2*i+1
        right = 2*i+2
        smallest = i

        # if left is in bounds and smaller
        if left < len(self.maxHeap) and self.maxHeap[left][1] < self.maxHeap[smallest][1]:
            smallest = left
        
        #same ^ but comparing w updated smallest index
        if right < len(self.maxHeap) and self.maxHeap[right][1] < self.maxHeap[smallest][1]:
            smallest = right

        #if smallest is NOT parent, swap and continue with subtree
        if smallest != i:
            # print("smallest: ", self.maxHeap[smallest])
            self.maxHeap[i],self.maxHeap[smallest] = self.maxHeap[smallest],self.maxHeap[i]
            self.heapify(smallest)

    #builds heap from given array
    def buildHeap(self, arr):
        self.maxHeap = arr

        #start from last index in array
        for i in range(len(arr), -1, -1):
            self.heapify(i)

        print()


    #builds heap from given array
    def printHeap(self):    
        for i in self.maxHeap:
            print(i[1], i[0], end=" / ")

def main():

    arr = [["the five", 2], ["nations", 5], ["attacked", 6], ["in harmony", 8], ["until the", 9], ["fire nation", 7], ["lived together", 3]] # 3 and 6 are suppose to swap once heapified
    myHeap = PriorityQueue()

    #build heap from array^
    myHeap.buildHeap(arr)
    myHeap.printHeap()

    myHeap.insert(["long ago", 1])
    print()
    myHeap.printHeap()

    myHeap.delete()
    print()
    myHeap.printHeap()

    print()
    print(myHeap.top())

    return 0

main()