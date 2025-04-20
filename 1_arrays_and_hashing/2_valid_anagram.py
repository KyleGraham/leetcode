#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Hash Map Solution
# time complexity: O(n + m)
# space complexity: O(1) since we have at most 26 different characters

#create 2 hash maps, one for each string
#loop through i to len of s
#add each character to the hash map of each string
#increment the value of the character in the hash map

#check that the hash maps are equal


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t