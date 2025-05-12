#Array question

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

#solution using euclidean algorithm
#time complexity O(m + n)
#space complexity O(m + n)

#first line checks if they don't share a gcd
# valid example:
# str1 = "ABC"
# str2 = "ABCABC"
# Invalid example:
# str1 = "AB"
# str2 = "ABCABC"

# str1 + str2 = str2 + str1
# valid: "ABCABCABC" = "ABCABCABC"
# invalid: "ABABCABC" = "ABCABCAB"

#rest is euclidean algorithm
#specific algorithm for finding gcd
#basically replace (a, b) with (b, a mod b)
#until b is 0, then a is the gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        len1 = len(str1)
        len2 = len(str2)

        while len2:
            len1, len2 = len2, len1 % len2
        return str1[:len1]