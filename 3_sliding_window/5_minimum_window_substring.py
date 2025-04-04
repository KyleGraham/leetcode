# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
#If such a substring does not exist, return an empty string "".

# optimum solution using sliding window
# time complexity: O(n)
# space complexity: O(n)
# calculate the character count of t, the shorter string or target string
# uses the number of unique characters in t as the need variable
# we then can check how many characters in the substring that match in the have var
# we then loop through the string and increment the count of the character in the substring
# if the count of the character in the substring is equal to the count of the character in t, increment the have variable
# if the have variable is equal to the need variable, we have found a substring that contains all the characters in t
#once the have and need match, document the substring and length if it's smaller than the current length
#then increment the L variable, if the have and need still match, document the substring, if they do not, increment the R variable
#return the substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        t_count = {}
        s_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        need = len(t_count)
        have = 0
        res = [-1, -1]
        res_len = float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] = 1 + s_count.get(c, 0)
            if c in t_count and s_count[c] == t_count[c]:
                have += 1
            while have == need:
                if res_len > r - l + 1:
                    res_len = (r - l + 1)
                    res = [l, r]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1 
        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ""