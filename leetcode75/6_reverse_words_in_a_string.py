
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words.
# Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

#one interviewers prob wont like
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


#one pass solution
#should be around O(n) time complexity

#some test cases have wierd spacing between words, thats why you gotta check if word before adding to result

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip()
        res = ""
        r = len(s) - 1
        while r >= 0:
            end = r
            while r >= 0 and s[r] != ' ':
                r -= 1
            start = r
            word = s[start+1:end+1]
            if word:
                res += word
                if not r == -1:
                    res += " "
            r -= 1
        return res