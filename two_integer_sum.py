#brute force solution
#time complexity: O(n^2)
#space complexity: O(1)
#loops through the array twice and checks if the sum of the two numbers is equal to the target
#since the indexes are based on 1 for some reason, we add 1 to the 0 index
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] != numbers[j] and numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                  

# optimal two pointer solution
# time complexity: O(n)
# space complexity: O(1)
# uses two pointers, one at the beginning and one at the end
#since values are sorted, you can do this like a binary search with the pointers
# if the sum is greater than the target, move the right pointer to the left
# if the sum is less than the target, move the left pointer to the right
# if the sum is equal to the target, return the indexes 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []