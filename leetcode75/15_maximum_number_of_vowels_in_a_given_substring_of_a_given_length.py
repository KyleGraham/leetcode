# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


#two pointer solution similar to one before
#time complexity: O(n)
#space complexity: O(1)

#basically same as previous question
#go through r to k in loop, fill curr with number of vowels present
#set res to curr
#loop through r from k to len(s)
#check if s[r] is a vowel, increment curr if so
#check if s[r-k] is a vowel, decrement curr if so since its outside the window now
#set res to max of res and curr


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = 0
        for r in range(k):
            if s[r] in vowels:
                curr += 1
        res = curr
        for r in range(k, len(s)):
            if s[r] in vowels:
                curr += 1
            if s[r - k] in vowels:
                curr -= 1
            res = max(res, curr)
        return res