# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
# You may return the solution in any order.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

#solution using backtracking
#time complexity: O(n * 2^n)
#space complexity: O(n) extra space, O(2^n) subsets

##essentially is going to be a decision tree where you can either include or not include a current number
#all substrings must be palindromes as well, so we can't ignore characters or anything

#initialize the result list
#initialize the part list
#both are state functions technically since the dfs is initialized in the function
#dfs function that takes in i as the current index
#check if the index is greater than or equal to the length of the list
#append the a copy of the part to the result list so it wont be modified by the next recursive call accessing it

#loop from i to the end of the string with var j
#check if the substring from i to j is a palindrome
#append the substring to the part list
#recursive call the function with the j index incremented by 1
#pop the substring from the part list
#call the dfs function with the index at 0

#function to check if palindrome

#uses the two indexes given l and r
#while l is less than r
#check if the characters at l and r are equal
# return false if they are not
#increment l and decrement r
#return true if the loop completes

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True