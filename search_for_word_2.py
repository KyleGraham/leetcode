
#essentially search_for_word.py + prefix tree

#solution using backtracking and prefix tree (trie)
#time complexity: O(M * n * 4 * 3^(t - 1) + s) where m is rows, n is cols, t is lenght of any word in words, and s is len of all words

#use the trienode and prefixtree class we made earlier

#in the findwords function
#initialize the rows and cols of the board
#initialize the path set
#initialize the prefix tree
#initialize the result list
#insert all the words into the prefix tree

#loop through all r of rows
#loop through all c of cols
#check if the prefix tree starts with the character at the row and col
#call the dfs function with the row and col and empty string

#the dfs function
#check if the substring is in the prefix tree
# if it is, check if the substring is not in the result list
# if it is not, append the substring to the result list
#do not return here, just incase the word extends to another word, like back and backend

#check if the row or col is out of bounds or the set exists in the path set
#return here if so

#add the row and col to the path set
#call the dfs function on every item to the right/left and top/bot of the cur item
#call the dfs function with the row + 1, col, and substring + board[r][c]
#call the dfs function with the row - 1, col, and substring + board[r][c]
#call the dfs function with the row, col + 1, and substring + board[r][c]
#call the dfs function with the row, col - 1, and substring + board[r][c]

#remove the row and col from the path set
#return


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        prefix_tree = PrefixTree()
        res = []
        for word in words:
            prefix_tree.insert(word)

        def dfs(r, c, substring):
            if prefix_tree.search(substring):
                if not substring in res:
                    res.append(substring)
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path):
                return 
            path.add((r, c))
            dfs((r + 1), c, substring + board[r][c])
            dfs((r - 1), c, substring + board[r][c])
            dfs(r, (c + 1), substring + board[r][c])
            dfs(r, (c - 1), substring + board[r][c])
            path.remove((r, c))
            return


        for r in range(ROWS):
            for c in range(COLS):
                if prefix_tree.startsWith(board[r][c]):
                    dfs(r, c, "")
        return res




        