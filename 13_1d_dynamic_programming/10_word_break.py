# Given a string s and a dictionary of strings wordDict, '
# return true if s can be segmented into a space-separated sequence of dictionary words.

# You are allowed to reuse words in the dictionary an unlimited number of times. 
# You may assume all dictionary words are unique.

# Example 1:
# Input: s = "neetcode", wordDict = ["neet","code"]
# Output: true
# Explanation: Return true because "neetcode" can be split into "neet" and "code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
# Output: true
# Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

# Example 3:
# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
# Output: false


#solution using dynamic programming bottom up
#time complexity: O(n * m * t) where n is len of string s, m is words in wordDict and t is max len of any word in wordDict
#space complexity: O(n)

#initialize dp as a list of False values with len(s) + 1
#base case is dp[len(s)] = True

#loop through the string from the end to the beginning
#for each word in the wordDict
#check if i + len of word is in bounds and if the substring of s from i to i + len(w) is equal to the word
#if so, set dp[i] to dp[i + len(w)], which will hit the base case of len(s) to start, or the true/false value at that index
#if we set that cache value to True, break
#return dp[0] since we want to know if the whole string can be segmented

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #start from last index. Compute if we can split from every index
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)] #will hit base case of len(s) to start
                if dp[i]:
                    break
        return dp[0]