
# You are given two strings s and t, both consisting of english letters.

# Return the number of distinct subsequences of s which are equal to t.

# Example 1:

# Input: s = "caaat", t = "cat"

# Output: 3
# Explanation: Rhere are 3 ways you can generate "cat" from s.

# (c)aa(at)
# (c)a(a)a(t)
# (ca)aa(t)
# Example 2:

# Input: s = "xxyxy", t = "xy"

# Output: 5
# Explanation: There are 5 ways you can generate "xy" from s.

# (x)x(y)xy
# (x)xyx(y)
# x(x)(y)xy
# x(x)yx(y)
# xxy(x)(y)


#solution using dynamic programming top down
#time complexity: O(n * m) where n is len(s) and m is len(t)
#space complexity: O(n * m) where n is len(s) and m is len(t)

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# start by initialize a hashmap for a dp cache

#dfs function, takes in i, j as the indexes in s, t
# check if j is at the end of t, if so return 1
# check if i is at the end of s, if so return 0 since we can't find t in s
# check if the key is in the cache, if so return the value
# check if the characters at the indexes are equal
# if so, set the cache value to the dfs of the next index in both strings plus the dfs of the next index in s and the cur index of j
#else, set the cache value to the dfs of the next index in s and the cur index of j
# return the cache value
# finally, return the dfs of 0, 0


def numDistinct(self, s: str, t: str) -> int:
    cache = {}

    def dfs(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        if s[i] == t[j]:
            cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            cache[(i, j)] = dfs(i + 1, j)
        return cache[(i, j)]
    return dfs(0, 0)