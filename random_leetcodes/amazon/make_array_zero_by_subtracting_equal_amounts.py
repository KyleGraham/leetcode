

#better solution
#will have to subtract for any unique value that isn't 0, so just make set and remove 0 if its in the set
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = set(nums)
        if 0 in n:
            n.remove(0)
        return len(n)



class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        subtract = 0
        for i, num in enumerate(nums.copy()):
            if num == 0 or (num - subtract) == 0 :
                continue
            subtract += (num - subtract)
            res += 1
        return res
