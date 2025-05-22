

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

#solution using Counters and sort
#Time complexity: O(nlog(n)) due to the sorts
#space complexity O(n) from the counters

#essentially we can use the two operations to change the order of the characters and change one character to another and vice versa
#so as long as the counts match, and the keys match, the rest doesn't matter



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        return sorted(count1.values()) == sorted(count2.values()) and sorted(count1.keys()) == sorted(count2.keys())
    