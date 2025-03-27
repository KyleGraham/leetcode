#sliding window algorithm optimal solution
# time complexity: O(n)
# space complexity: O(n)
#uses set to hold unique characters in substring
#uses two pointers to keep track of the start and end of the substring
#loops through the string with the right pointer
#if a duplicate is found, removes the value at the left pointer and increments the left pointer until the duplicate is removed
#adds the value at the right pointer to the set
#calculates the length of the substring and returns the longest substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res