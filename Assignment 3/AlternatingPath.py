from collections import defaultdict, deque

def alternating_path(paths, origin, destination):
    graph = defaultdict(list)
    for start, end, color in paths:
        graph[start].append((end, color))
    
    q = deque()
    q.append((origin, 0, None)) # current origin, length, color
    print(graph)
    while q:
        curr_origin, length, color = q.popleft()
        if curr_origin == destination:
            return length 
        for next_dest, next_color in graph[curr_origin]:
            if next_color != color:
                q.append((next_dest, length + 1, next_color))
    
    return -1
    

def main():
    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 
                            'A', 'E'))
    # Output: 4
    # Path: A→D (red), D→C (blue), C→B (red), B→E (blue))

    print(alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), 
                            ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), 
                            ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 
                            'E', 'D'))
    # Output: -1
    # Invalid path: E→C (red), C→B (red), B→D (blue)


main()


"""
Graph = {
    'A': [('B', 'blue'), ('C', 'red'), ('D', 'red')], 
    'B': [('D', 'blue'), ('E', 'blue')], 
    'C': [('B', 'red')], 
    'D': [('C', 'blue'), ('E', 'red')], 
    'E': [('C', 'red')]
    }
"""