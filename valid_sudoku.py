# brute force solution
# time complexity: O(n^2)
# space complexity: O(n^2)
# loop through every item in the board
# check if the item exists in the hashmap of rows, columns, or boxes
# boxes uses // (floor division and assign) to get the box the item is in
# if the item exists in the hashmap, return False
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
      cols = collections.defaultdict(set)
      rows = collections.defaultdict(set)
      boxes = collections.defaultdict(set)
      
      for i in range(9):
          for j in range(9):
              if board[i][j] == '.':
                  continue
              if (board[i][j] in rows[i] or
                  board[i][j] in cols[j] or
                  board[i][j] in boxes[(i//3, j//3)]):
                  return False
              cols[j].add(board[i][j])
              rows[i].add(board[i][j])
              boxes[(i//3, j//3)].add(board[i][j])
      return True