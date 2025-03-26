# Hash Map Solution
# time complexity: O(n + m)
# space complexity: O(1) since we have at most 26 different characters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        return hash_s == hash_t