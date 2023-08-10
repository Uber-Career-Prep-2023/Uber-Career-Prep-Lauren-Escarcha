# DFS

# Time complexity = O(n * 8^m) where n is total number of cells and m is average word length

# Space complexity = O(m) where m is the number of words
# Technically the worst case would be that every single word
# is possibly present in the board. 

def boggle(board, dictionary):

    # creates dictionary of words in all upper case
    dictionary_set = set(word.upper() for word in dictionary)
    valid_words = set()
    
    # performs a DFS of all possible word combinations
    def dfs(x, y, visited, word):
        visited.add((x, y))
        word += board[x][y]

        # if the word is valid, then adds the word to visited
        if len(word) >= 3 and word in dictionary_set:
            valid_words.add(word)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < len(board)) and (0 <= new_y < len(board[0])) and (new_x, new_y) not in visited:
                    dfs(new_x, new_y, visited.copy(), word)

    
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, set(), '')

    # 
    return sorted(list(valid_words))

# Example
dictionary = {
    "Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace",
    "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Rap", "Ray",
    "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"
}

board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"]
]

output = boggle(board, dictionary)
print(output)