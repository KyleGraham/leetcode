
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

#solution using sets
#time complexity O(n)
#space complexity O(n)

#create a counter.
#loop through values
#set cur val to -1
#check if the value exists in the set
#since the cur value will not be the same, only other keys with the same val will return true here
#return false if its found
#set the value back


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for key, val in count.items():
            count[key] = -1
            if val in count.values():
                return False
            count[key] = val
        return True