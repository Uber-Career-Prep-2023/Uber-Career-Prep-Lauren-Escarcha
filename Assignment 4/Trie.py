# Space Complexity = O(m*n) where m is number of words in the trie and n is the avg word length

# Time Complexity = O(word length) for insert, valid_word and O(longest word length) for remove


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def isValidWord(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end == True

    def remove(self,word):
        def _remove(node, word, index):
            if index == len(word):
                node.end = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child_node = node.children[char]
            should_remove_child = _remove(child_node, word, index + 1)

            if should_remove_child:
                del node.children[char]
                return len(node.children) == 0 and not node.end

            return False

        _remove(self.root, word, 0)

if __name__ == '__main__':
    new_trie = Trie()
    new_trie.insert('team')
    new_trie.insert('teal')
    new_trie.insert('ten')
    new_trie.insert('tee')
    new_trie.insert('tenet')
    
    assert new_trie.isValidWord('team') == True
    assert new_trie.isValidWord('teal') == True
    assert new_trie.isValidWord('ten') == True
    assert new_trie.isValidWord('tee') ==True
    assert new_trie.isValidWord('tenet') == True
    assert new_trie.isValidWord('teas') == False

    new_trie.remove('tenet')
    assert new_trie.isValidWord('tenet') == False
    new_trie.remove('team')
    assert new_trie.isValidWord('team') == False
    new_trie.remove('ten')
    assert new_trie.isValidWord('ten') == False

    print('Testing Completed')