from collections import deque

def first_k_binary(k):
    if k <= 0: return []

    res = ['0']
    q = deque()
    q.append('1')

    while len(res) < k:
        num = q.popleft()
        if num:
            res.append(num)
        q.append(num + '0')
        q.append(num + '1')

    return res

def main():
    print(first_k_binary(5))    # Output: ['0', '1', '10', '11', '100']
    print(first_k_binary(10))   # Output: ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']

main()