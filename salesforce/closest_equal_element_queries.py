# You are given a circular array nums and an array queries.

# For each query i, you have to find the following:

# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. 
# If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

# Example 1:

# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

# Output: [2,-1,3]

# Explanation:

# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1,
#  and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
# Example 2:

# Input: nums = [1,2,3,4], queries = [0,1,2,3]

# Output: [-1,-1,-1,-1]

# Explanation:

# Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

 

# Constraints:

# 1 <= queries.length <= nums.length <= 105
# 1 <= nums[i] <= 106
# 0 <= queries[i] < nums.length



#solution using hashmap
#time complexity O(n)
#space complexity O(n)

#essentially we want the distance between a given number and any other number in the array

#so we fill a default dict with the positions of all the numbers in nums

#nums = [6,12,17,9,16,7,6]
#defaultdict(<class 'list'>, {6: [0, 6], 12: [1], 17: [2], 9: [3], 16: [4], 7: [5]})

#next step we replace the values at the indexes of nums with the distance to it's closest match

#we loop through the arrays in that default dict's values
#if that array only contains 1 value, there's no matches so set the nums at that position to -1
#if it contains more than 1 value
#we loop through the values
#set f and b to the value to the left and right, with a mod of the size of the num of values for overflow
#set forward to the min of the len of nums, the cur value, and f, along with the abs of the value minus f
#set backward to the min of the abs of the b val minus the cur val and cur plus the total nums minus the b val

#set the value of the index of nums to the min of forward and backward

#then fill the queries array up with the answer at the given index
#loop through i in range len queries
#queries [i] = nums[queries[i]]

#return queries





class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        for arr in pos.values():
            m = len(arr)
            if m == 1:
                nums[arr[0]] = -1
                continue
            for i in range(m):
                cur = arr[i]
                f, b = arr[(i + 1) % m], arr[(i - 1 + m) % m]
                forward = min(n - cur + f, abs(cur - f))
                backward = min(abs(b - cur), cur + (n - b))
                nums[arr[i]] = min(backward, forward)
        for i in range(len(queries)):
            queries[i] = nums[queries[i]]
        return queries