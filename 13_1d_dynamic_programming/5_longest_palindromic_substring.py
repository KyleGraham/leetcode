# Given a string s, return the longest substring of s that is a palindrome.
# A palindrome is a string that reads the same forward and backward.
# If there are multiple palindromic substrings that have the same length, return any one of them.

# Example 1:
# Input: s = "ababd"
# Output: "bab"
# Explanation: Both "aba" and "bab" are valid answers.

# Example 2:
# Input: s = "abbc"
# Output: "bb"



#I think this solution is better
#time complexity: O(n^2)
#space complexity: O(1)
#this solution uses two pointers to check for palindromes
#it checks for odd and even length palindromes
#it starts at the middle of the string and expands outwards
#it checks if the left and right characters are equal

#initialize res as empty string
#initialize resLen as 0
#loop through the string starting at 0
#check odd lengths
#initialize left and right pointers as i and i
#while loop that checks if the left and right pointer are in bounds and that s[l] == s[r]
# if they are, check if the length of the palindrome is greater than resLen
# if it is, set res to the palindrome and resLen to the length of the palindrome
#setting is basicaly s[l:r+1] since r is inclusive. This sets it from l to r + 1
#set resLen to the new length
#decrement left and increment right
#check even lengths
#basically does the same thing, but we set the left pointer to i and the right pointer to i + 1
#exact same while loop

#return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
