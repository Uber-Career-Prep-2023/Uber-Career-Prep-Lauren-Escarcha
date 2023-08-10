# DP Memorization

# Time complexity = O(n)

# Space Complexity = O(n)

def minCostStairClimbing(costs):
    n = len(costs)
    if n == 0:
        return 0
    if n == 1:
        return costs[0]
    
    # list of all costs
    min_cost = [0] * n
    
    min_cost[0] = costs[0]
    min_cost[1] = costs[1]
    
    # Calculate the minimum cost to reach each stair from the ground by 
    # comparing possible steps taken to get to current step
    for i in range(2, n):
        min_cost[i] = costs[i] + min(min_cost[i-1], min_cost[i-2])
    
    
    return min(min_cost[n-1], min_cost[n-2])


print(minCostStairClimbing([4, 1, 6, 3, 5, 8]))  # 9
print(minCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))  # 25