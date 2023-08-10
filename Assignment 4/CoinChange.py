# DP

# Time Complexity = O(n * m)

# Space Complexity = O(m)

def coinChange(coins, target_sum):

    dp = [0] * (target_sum + 1)
    dp[0] = 1  

    # Iterate through each coin 
    for coin in coins:
        # Update the dp array for each sum
        for i in range(coin, target_sum + 1):
            dp[i] += dp[i - coin]

    return dp[target_sum]

# Test cases
print(coinChange([2, 5, 10], 20))  # Output: 6
print(coinChange([2, 5, 10], 15))  # Output: 3