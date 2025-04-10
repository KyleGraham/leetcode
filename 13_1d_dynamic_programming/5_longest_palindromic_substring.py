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



#my solution using 2 pointers
##time complexity: O(n^2)
##space complexity: O(1)

#basically we start in the middle of the string and expand outwards
#but edge cases like aa or aaaaaaa are handled by the first while loop
#we check if the left or right are equal to the middle and add them to the temp string, so with repeat characters in the middle
#we gather all of them before expanding outwards

#check if len(s) is 1, if so return s
#initialize res as empty string
#loop through the string starting at 1
#initialize left and right pointers as i - 1 and i + 1
#initialize temp as s[i]
#while the left pointer is greater than or equal to 0 and the character at the left pointer is equal to s[i]
#or the right pointer is less than or equal to the length of s - 1 and the character at the right pointer is equal to s[i]
#check if the left pointer is greater than or equal to 0 and the character at the left pointer is equal to s[i]
# if so, add the character at the left pointer to temp and decrement the left pointer
#check if the right pointer is less than or equal to the length of s - 1 and the character at the right pointer is equal to s[i]
# if so, add the character at the right pointer to temp and increment the right pointer

#check if the length of temp is greater than the length of res
# if so, set res to temp
#while the left pointer is greater than or equal to 0 and the right pointer is less than or equal to the length of s - 1
#and the character at the left pointer is equal to the character at the right pointer
#add the left character to the left side of temp and the right character to the right side of temp
#check if the length of temp is greater than the length of res
# if so, set res to temp
#decrement the left pointer and increment the right pointer
#return res outside the loop


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        for i in range(1, len(s)):
            l = i - 1
            r = i + 1
            temp = s[i]
            while l >= 0 and s[l] == s[i] or r <= len(s) - 1 and s[r] == s[i]:
                if l >= 0 and s[l] == s[i]:
                    temp = s[l] + temp
                    l -= 1
                if r <= len(s) - 1 and s[r] == s[i]:
                    temp = temp + s[r]
                    r += 1
            if len(temp) > len(res):
                res = temp
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                temp = s[l] + temp + s[r]
                if len(temp) > len(res):
                    res = temp
                l -= 1
                r += 1
        return res
