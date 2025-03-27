#You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

#sliding window
# keeps two hashes, one for the smaller string s1 that is caculated initially, and one for the larget string s2
# creates two pointers both at 0
# loops through the larger string
# adds the larger strings character to the hash 
#checks if both hashes are equal, returns true if they are
# checks if the length of the substring is equal to the length of s1
# if so, decrements the count of the character at the left pointer and increments the left pointer
# returns false if no permutation is found
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        smallCount = {}
        bigCount = {}
        for c in s1:
            smallCount[c] = 1 + smallCount.get(c, 0)
        for r in range(len(s2)):
            bigCount[s2[r]] = 1 + bigCount.get(s2[r], 0)
            if bigCount == smallCount:
                return True
            elif r - l + 1 == len(s1):
                bigCount[s2[l]] -= 1
                if bigCount[s2[l]] == 0:
                    bigCount.pop(s2[l])
                l += 1
                
            
        return False