# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.



# Example 1:
# Input: digits = "34"
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

# Example 2:
# Input: digits = ""
# Output: []

#solution using backtracking
#time complexity: O(n * 4^n)
#space complexity: O(n). O(4^n) for the result list

#check if the digits string is empty
#return empty list if so

#initialize the result list
#initialize the digit to character mapping
#initialize the dfs function with i as the current index and curStr as the current string
#check if the length of the current string is equal to the length of the digits string
#append the current string to the result list and return
#loop through the characters mapped to the current digit
#recursive call the function with the current index + 1 and the current string + the character
#call the dfs function with the index at 0 and an empty string
#return res


class Solution:
  
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        

        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
        dfs(0, "")
        return res