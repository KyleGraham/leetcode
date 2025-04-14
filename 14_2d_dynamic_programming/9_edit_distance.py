# You are given two strings word1 and word2, each consisting of lowercase English letters.

# You are allowed to perform three operations on word1 an unlimited number of times:

# Insert a character at any position
# Delete a character at any position
# Replace a character at any position
# Return the minimum number of operations to make word1 equal word2.

# Example 1:
# Input: word1 = "monkeys", word2 = "money"
# Output: 2
# Explanation:
# monkeys -> monkey (remove s)
# monkey -> monkey (remove k)

# Example 2:
# Input: word1 = "neatcdee", word2 = "neetcode"

# Output: 3
# Explanation:
# neatcdee -> neetcdee (replace a with e)
# neetcdee -> neetcde (remove last e)
# neetcde -> neetcode (insert o)

#soution using dynamic programming bottom up
#time complexity: O(n * m) where n is len of word1 and m is len of word2
#space complexity: O(n * m) where n is len of word1 and m is len of word2
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# essentially we use a 2d array to keep track of the number of operations needed to convert word1 to word2
#in the 2d array, [i + 1][j] is insertion, [i][j + 1] is deletion, and [i + 1][j + 1] is replacement
#the extra row is the basecase of the empty string which is 0, then the deletions if one is empty or inserts if one is empty
  #a c d  
#a 1      3
#b   1    2
#d      0 1
#  3 2  1 0

#initialize cache as a 2d array of len(word2 + 1) and len(word1 + 1) with initial value of float infinity

#loop through the array and set the last row to the length of word2 - j
#loop through the array and set the last column to the length of word1 - i

#loop through each string in reverse
#if they are equal, return the cache value of i + 1, j + 1
#otherwise, set the cache value to 1 + the min of the three operations
#return the cache value of 0, 0


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [ [[float('infinity')]] * (len(word2) + 1) for i in range(len(word1) + 1)] 
        
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    #                     insert            delete              replace
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        return cache[0][0]