import collections
class Solution:    

    def NumberOfIslands(self, grid: list[list[int]]):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        #function within function
        def bfs(row, col):
            #iterative 
            queue = collections.deque()
            visit.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for downRow, downCol in directions:

                    row = row + downRow
                    col = col + downCol

                    if ((row) in range(rows) and 
                        (col) in range(cols) and 
                        grid[row][col] == 1 and 
                        (row, col) not in visit):
                            queue.append((row, col))
                            visit.add((row, col))
                    

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1

        return islands        


def main():

    solution = Solution()

    board = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(solution.NumberOfIslands(board)) # Output: 3

    board = [
        [1, 0, 0],
        [0, 0, 0]
    ]
    print(solution.NumberOfIslands(board)) # Output: 1

main()