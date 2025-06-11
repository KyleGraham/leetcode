# Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some 
# or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.

# Example 1:

# Input: text1 = "cat", text2 = "crabt" 

# Output: 3 
# Explanation: The longest common subsequence is "cat" which has a length of 3.

# Example 2:

# Input: text1 = "abcd", text2 = "abcd"

# Output: 4
# Example 3:

# Input: text1 = "abcd", text2 = "efgh"

# Output: 0

#solution using dynamic programming with backtracking and a cache
#time complexity: O(n * m) where n is len of text1 and m is len of text2
#space complexity: O(n * m) where n is len of text1 and m is len of text2

#we start by initializing a 2d array of 0s with len(text1) + 1 and len(text2) + 1, this defaults out of bounds to 0 as well
#then we loop through the array from the bottom right to the top left
#for each index, we check if the characters at that index are equal
#and if so, we set the current index to 1 + the next index in both dimensions moving diagonally
#otherwise, we set the current index to the max of the right and down indexes
#at the end, we return the top left index, which is the length of the longest common substring


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        one = len(text1)
        two = len(text2)
        dp = [[0 for j in range(two + 1)]
                for i in range(one + 1)]

        for r in range(one -1, -1, -1):
            for c in range(two - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]