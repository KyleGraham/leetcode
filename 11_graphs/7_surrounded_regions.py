# You are given a 2-D matrix board containing 'X' and 'O' characters.

# If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

# Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

# Example 1:
# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]
# Explanation: Note that regions that are on the border are not considered surrounded regions.


#bfs solution
#time complexity O(m * n) where m is number of rows and n is number of cols
#space complexity O(m * n)

#essentially, and O is surrounded by Xs if we cannot reach the edge of the board from an O
#so we loop through rows and cols and calls bfs if the item is an O and it is not in visted

#the bfs function
#takes in r, c
#creates a deque
#appends the item to the deque
#creates a group deque. This will hold the Os that are next to eachother 
#initialize a surrounded boolean to True

#loop through the queue
#pop the left item from the queue to get row and col
#add the item to the visited set
#append the item to the group deque
#loop through the directions list
#initialize new row and col variables taking the row/col from the queue and adding the directions row/col
#check if the new row and col are in range of the grid
#if they are not in the range of the grid, the group is not surrounded. Change surrounded bool to False

#check if the new row and col is not in the visited set and the item is an O
# if so, append the new row and col to the queue

#outside the q loop, check if the group is surrounded
#if so, loop through the group q
#pop each row and col and set the board at that row and col to an X



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        os = set()
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            group = deque()
            surrounded = True
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                group.append((row, col)) 
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols):
                            surrounded = False
                    elif (nr, nc) not in visited and board[nr][nc] == "O":
                        q.append((nr, nc))
            if surrounded:
                while group:
                    row, col = group.popleft()
                    board[row][col] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not (r, c) in visited:
                    bfs(r, c)
                    
        



            
        






