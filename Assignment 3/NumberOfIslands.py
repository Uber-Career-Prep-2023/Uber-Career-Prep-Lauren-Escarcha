def num_islands(board):

    ROWS, COLS = len(board), len(board[0])
    count = 0

    def dfs(row, col):
        # return if not connecting square
        if row >= ROWS or row < 0 or col >= COLS or col < 0:
            return
        if board[row][col] != 1:
            return
        # mark neighboring islands so won't revisit
        board[row][col] = 'X'
        
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        
    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                count += 1
                dfs(r, c)

    return count


def main():
    board = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(num_islands(board)) # Output: 3

    board = [
        [1, 0, 0],
        [0, 0, 0]
    ]
    print(num_islands(board)) # Output: 1

main()