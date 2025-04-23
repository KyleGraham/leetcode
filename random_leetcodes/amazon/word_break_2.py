# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word
# is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

#solution using recursion and memoization
#time complexity: O(2^n)
#space complexity: O(2^n)

#make the word dict a word set
#initialize a memoization dict
#initialize a helper function that takes in the start index
#initialize a valid substr list
#check if the start index is at the end of the string
# if so, append an empty string to the valid substr list
#loop through the string from start + 1 to len(s) + 1
#for each end index, get the prefix substring
#check if the prefix is in the word set
# if so, call the helper function with the end index
#and get the suffixes
#for each suffix, append the prefix and suffix to the valid substr list
#set memo[start] to the valid substr list
#return the valid substr list

#return the helper function with the start index of 0

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def helper(start):
            if start in memo:
              return memo[start]
            valid_substr = []

            if start == len(s):
                valid_substr.append("")
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in word_set:
                    suffixes = helper(end)
                    for suffix in suffixes:
                        valid_substr.append(prefix + ("" if suffix == "" else " ") + suffix)
            memo[start] = valid_substr
            return valid_substr
        
        return helper(0)
