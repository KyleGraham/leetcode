#You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.
#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

#sliding window solution
#time complexity O(n + m) n = length of string, m = total number of unique characters
#space complexity O(m)
#uses two pointers to keep track of the start and end of the substring
#uses a dictionary to keep track of the count of characters in the substring
#checks if the length of the substring minus the maximum count of a character is greater than k
#decrements the count of the character at the left pointer and increments the left pointer if so
#returns the longest substring

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max (res, r - l + 1)
        return res
            