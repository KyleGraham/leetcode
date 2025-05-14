# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?



#two pointer solution, but with the pointers at each string
#Time complexity: O(n)
#space complexity: O(1)

#Essentially, we have a left pointer for s, and a right pointer for t
#initialize the size of s and t for our l_size and r_size
#while loop while l < l_size and r < r_size
#if the characters match, increment both. Otherwise only increment right
#return if the left pointer made it to the end of s


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l_size = len(s)
        r_size = len(t)
        l = r = 0
        while l < l_size and r < r_size:
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == l_size