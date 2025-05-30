# You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. 
# You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

# To obtain target, you may apply the following operation on triplets zero or more times:

# Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

# Return true if it is possible to obtain target as an element of triplets, or false otherwise.

# Example 1:
# Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
# Output: true
# Explanation:
# Choose the first and second triplets, update the second triplet to be [max(1, 7), max(2, 1), max(3, 1)] = [7, 2, 3].

# Example 2:
# Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
# Output: false

#greedy solution
#time complexity: O(n)
#space complexity: O(1)

#biggest takeaway is that if a triplet has any value higher than the target at the same index, we can ignore it
#after we know we can use the triplet, we check if an index has a value equal to the target value at the index
#if so, we add it to the set since we have a match
#finally, we check if the set has all 3 indexes, if so return True


#initialize good as a set
#loop through the triplets
#check if the triplet has any value higher than the target at the same index
# if so, continue
#loop through the triplet with enumerate
#check if the value is equal to the target at the index
# if so, add the index to the set
#finally, check if the set has all 3 indexes, if so return True


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3