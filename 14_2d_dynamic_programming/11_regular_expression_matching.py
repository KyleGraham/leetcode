# You are given an input string s consisting of lowercase english letters, 
# and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

# Return true if the pattern matches the entire input string, otherwise return false.

# '.' Matches any single character
# '*' Matches zero or more of the preceding element.
# Example 1:

# Input: s = "aa", p = ".b"

# Output: false
# Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

# Example 2:

# Input: s = "nnn", p = "n*"

# Output: true
# Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

# Example 3:

# Input: s = "xyz", p = ".*z"

# Output: true
# Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".





#solution using top down memoization
#time complexity: O(n * m) where n is len(s) and m is len(p)
#space complexity: O(n * m) where n is len(s) and m is len(p)

#essentially, we are checking if the string s matches the pattern p, which can contain . or *
# . matches any single character
# * matches zero or more of the preceding element

#mainly we check if the patterns next character is a *
#if it is, we can either ignore the * and the preceding character or we can use the preceding character and check if it matches the current character in s


#start by initializing cache as a hashmap
#initialize a dfs function that takes in i and j as the indexes of s and p
#check if the key is in the cache, if so return the value
#check if both indexes are at the end of the string, if so return True
#check if the pattern index is at the end of the string, if so return False
#initialize match as True if the indexes are in bounds and the characters are equal or the pattern character is a .
#check if the next character in the pattern is a *
#if so, set the cache of the indexes to:
# dfs current index i and j + 2 this is if we don't use the star 
#or match and dfs current index i + 1 and j this is if we use the star
#if either are true because of the or, then we set the cache to True and return the cache

# if the match is True, set the cache to the dfs of the next index in both strings
# if not, set the cache to False
# return the cache value

# finally, return the dfs of 0, 0



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #top down memoization
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or         #dont use star
                    (match and dfs(i + 1, j)))    #use star
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
            


