# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.


# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]



#solution using dynamic programming
#time complexity: O(m^3 * n) where m is the length of the longest word and n is the number of words
#space complexity: O(n * m) where m is the length of the longest word


# Put all the words into a HashSet as a dictionary.
# Create an empty list answer.
# For each word in the words create a boolean array dp of length = word.length + 1, and set dp[0] = true.
# For each index i from 1 to word.length, set dp[i] to true if we can find a value j from 
# 0 (1 if i == word.length) such that dp[j] = true and word.substring(j, i) is in the dictionary.
# Put word into answer if dp[word.length] = true.
# After processing all the words, return answer.


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        answer = []
        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            
            for i in range(1, length+1):
                for j in range((i == length) and 1 or 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in dictionary
            if dp[length]:
                answer.append(word)
        return answer