# You are given a string s consisting of lowercase english letters.

# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

# Return a list of integers representing the size of these substrings in the order they appear in the string.

# Example 1:
# Input: s = "xyxxyzbzbbisl"
# Output: [5, 5, 1, 1, 1]
# Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

# Example 2:
# Input: s = "abcabc"
# Output: [6]



#greedy solution
#time complexity: O(n)
#space complexity: O(1)

#essentially, we cannot stop a subarray until we reach the last index of any character in the subarray
#this is so the characters don't repeat in subarrays

#first we initialize a hashmap lastIndex
#then loop through the string with an enumerate. We get the lastIndex of each character to the index
#this gives us a dictionary of the last index of each character
#then we initialize res as an empty list, size as 0 and end as 0
#then we loop through the string again with an enumerate
#increment size by 1
#set end to the max of end and the last index of the current character
#check if the current index is equal to the end
# if so, append size to res and set size to 0
#return res at the end


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
      