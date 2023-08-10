# DP Memorization

# Time comeplxity = O(n^2)

# Space complexity = O(n)

def generate_catalan_numbers(n):
    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            catalan_numbers[i] += catalan_numbers[j] * catalan_numbers[i - j - 1]

    return catalan_numbers

# Test examples
print(generate_catalan_numbers(1))  # Output: [1, 1]
print(generate_catalan_numbers(5))  # Output: [1, 1, 2, 5, 14, 42]