from collections import defaultdict, deque
def VacationDestinations(destinations, origin, k):
    adjList = defaultdict(list)
    res = []
    for city1,city2,time in destinations:
        adjList[city1].append((city2,time))
        adjList[city2].append((city1,time))

    q = deque([(origin,-1)])
    visited = set([origin])
    while q:
        curr, time = q.popleft()
     
        if time <= k and time != -1:
            res.append(curr)
        
        for neighbor, newTime in adjList[curr]:
            if neighbor not in visited:
                q.append((neighbor,time+newTime+1))
                visited.add(neighbor)
    return res

input = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

print(VacationDestinations(input, "New York",5))
print(VacationDestinations(input, "New York",7))
print(VacationDestinations(input, "New York",8))
'''
Time spent: 20 mins
'''