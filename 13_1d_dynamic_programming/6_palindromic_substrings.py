# Given a string s, return the number of substrings within s that are palindromes.

# A palindrome is a string that reads the same forward and backward.

# Example 1:

# Input: s = "abc"

# Output: 3
# Explanation: "a", "b", "c".

# Example 2:

# Input: s = "aaa"

# Output: 6
# Explanation: "a", "a", "a", "aa", "aa", "aaa". 
# Note that different substrings are counted as different palindromes even if the string contents are the same.


#solution using 2 pointers
#really similar to longest_palindromic_substring.py
#time complexity: O(n^2)
#space complexity: O(1)

#the idea here is that each while loop will find any odd or even length palindromes
#and count them
#the odd catches characters that are length 1 as well 

#initialize res as 0
#loop through the string starting at 0
#check odd lengths
#initialize left and right pointers as i and i
#while loop that checks if the left and right pointer are in bounds and that s[l] == s[r]
# if they are, increment res
#decrement left and increment right
#check even lengths
#basically does the same thing, but we set the left pointer to i and the right pointer to i + 1
#exact same while loop

#return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res