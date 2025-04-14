# You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

# Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

# |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
# You may assume that s1, s2 and s3 consist of lowercase English letters.

# Example 1:



# Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

# Output: true
# Explanation: We can split s1 into ["aa", "aa"], s2 can remain as "bbbb" and s3 is formed by interleaving ["aa", "aa"] and "bbbb".

# Example 2:

# Input: s1 = "", s2 = "", s3 = ""

# Output: true
# Example 3:

# Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

# Output: false


# make a matrix chart with s1 + 1 on top and s2 + 1 on the left, stores True or False


#dynamic programming bottom up solution
#time complexity O(n * m) where n is len(s1) and m is len(s2)
#space complexity O(n * m) where n is len(s1) and m is len(s2)

#start by checking if the length of s1 + s2 is not equal to s3
#return false if so
#initialize a 2d array of False values with len(s1) + 1 and len(s2) + 1
#the last index is set to True since we are checking if the last index of s3 is equal to the last index of s1 and s2
#loop through the characters in s1 and s2 in reverse order
#check if i is in len of s1 and s1[i] == s3[i + j] and dp[i + 1][j] is True
#then set dp[i][j] to True
#check if j is in len of s2 and s2[j] == s3[i + j] and dp[i][j + 1] is True
#then set dp[i][j] to True
#return dp[0][0] since we want to know if the whole string can be interleaved


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]   




#recursive memoization solution


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        #k = i + j

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
            return False
        return dfs(0, 0)