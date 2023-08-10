import math

class MinHeap:
    
    def __init__(self):
        self.minHeap = []

    def top(self):
        return self.minHeap[0]

    def insert(self, num):
        #1 - add element to end (rightmost of last level)
        self.minHeap.append(num)

        #index of inserted num and given parents
        child = len(self.minHeap) - 1
        parent = math.floor((child-1)/2)

        #HEAPIFY UP:
        #while not root
        #and parent is LESS than child
        while(child > 0 and self.minHeap[int(parent)] > self.minHeap[child]):
            #swap 

            self.minHeap[(parent)], self.minHeap[child] = self.minHeap[child], self.minHeap[(parent)]
            child = parent
            parent = math.floor((child-1)/2)

        #TODO: do I need this or can I just call heapify^?

    def delete(self):
        #edge case
        if self.minHeap is None or len(self.minHeap) == 0:
            return

        #1 - move last element to root (and delete og root value)
        self.minHeap[0] = self.minHeap[len(self.minHeap)-1]

        #2 - delete the last index, decrease size
        self.minHeap.pop()

        #3 - heapify to maintain order
        self.heapify(0)


    #build heap from array = start from back of array
    #delete node in heap = start from beginning of array
    def heapify(self, i):

        left = 2*i+1
        right = 2*i+2
        smallest = i

        # if left is in bounds and smaller
        if left < len(self.minHeap) and self.minHeap[left] < self.minHeap[smallest]:
            smallest = left
        
        #same ^ but comparing w updated smallest index
        if right < len(self.minHeap) and self.minHeap[right] < self.minHeap[smallest]:
            smallest = right

        #if smallest is NOT parent, swap and continue with subtree
        if smallest != i:
            # print("smallest: ", self.minHeap[smallest])
            self.minHeap[i],self.minHeap[smallest] = self.minHeap[smallest],self.minHeap[i]
            self.heapify(smallest)

    #builds heap from given array
    def buildHeap(self, arr):
        self.minHeap = arr

        #start from last index in array
        for i in range(len(arr), -1, -1):
            self.heapify(i)

        print()


    #builds heap from given array
    def printHeap(self):    
        for i in self.minHeap:
            print(i, end=" ")

def main():

    arr = [2,5,6,8,9,7,3] # 3 and 6 are suppose to swap once heapified
    myHeap = MinHeap()

    #build heap from array^
    myHeap.buildHeap(arr)
    myHeap.printHeap()

    myHeap.insert(1)
    print()
    myHeap.printHeap()

    myHeap.delete()
    print()
    myHeap.printHeap()

    print()
    print(myHeap.top())

    return 0

main()