class AdjacencyList:
    def __init__(self):
        pass

    #global variables 
    graph = {} #graph = map of sets
    vertices = 0 #num of vert


    # --- TIME COMPLEXITY: O(V+E)
    # --- SPACE COMPLEXITY: O(V^2), where every node is connected to every other node
    def buildGraph(self, edges):

        #loops thru each pair and makes connection
        #will only connect first 2 indexes, since it's a pair
        for pair in edges:
            self.buildConnection(pair[0], pair[1])
    
    #connects edge start and end
    def buildConnection(self, start, end):
        if self.graph.get(start):
            #if key was inserted before, add new edge
            #duplicates will be ignored since edges are in a set
            self.graph[start].add(end)

        else:
            #make new key and corresponding set of edges
            self.graph.update({start: {end}})

        if self.graph.get(end) is None:
            #if end is not a key itself, add
            self.graph.update({end: set()})

    def DFS(self):
        #starts at first node in map, can be any node
        self.vertices = len(self.graph)
        visited = set()

        self.DFShelper(list(self.graph.keys())[0], visited)

    def DFShelper(self, vertice, visited):
        #can start at any node
        visited.add(vertice)
        print(vertice, " ")

        for neighbor in self.graph[vertice]:
            if neighbor not in visited:
                self.DFShelper(neighbor, visited)

    
    def printGraph(self):

        #print SORTED, dict is originally unsorted
        for key in sorted(self.graph.keys()):
            print(key, end=': ') #print key

            #loop through set of edges
            for edge in self.graph[key]:
                print(edge, end=' ') #print edge
            
            print()

def main():
    graph = AdjacencyList()

    graph.buildGraph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
    graph.printGraph()

    graph.DFS()

main()


    

