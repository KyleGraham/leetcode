# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice,
# and the combinations may be returned in any order.

 

# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

# Constraints:

# 2 <= k <= 9
# 1 <= n <= 60



#solution using backtracking
#Time complexity: O(K×9!) or O(K×C(9,K)) 9 factorial with k distinct numbers
#space complexity: O(K)

# To implement the algorithm, one could literally follow the steps in the Intuition section.
# However, we would like to highlight a key trick that we employed, 
# in order to ensure the non-redundancy among the digits within a single combination, as well as the non-redundancy among the combinations.

# The trick is that we pick the candidates in order.
# We treat the candidate digits as a list with order, i.e. [1, 2, 3, 4, 5, 6, 7, 8. 9].
# At any given step, once we pick a digit, e.g. 6, we will not consider any digits before the chosen digit for the following steps,
#     e.g. the candidates are reduced down to [7, 8, 9].

# With the above strategy, we could ensure that a digit will never be picked twice for the same combination.
# Also, all the combinations that we come up with would be unique.


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []

        def dfs(i, cur):
            if cur and sum(cur) == n:
                if (len(cur) == k):
                    res.append(cur)
                return
            
            if i >= len(candidates):
                return
            
            dfs(i + 1, cur + [candidates[i]])
            dfs(i + 1, cur)
        dfs(0, [])
        return res