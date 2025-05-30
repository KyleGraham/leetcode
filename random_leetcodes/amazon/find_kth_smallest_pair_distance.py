


#brute force solution

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        minH = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                heapq.heappush(minH, (abs(nums[i] - nums[j]), (nums[i], nums[j])))
        for i in range(len(minH)):
            val, indexes = heapq.heappop(minH)
            if i + 1 == k:
                return val
              
              
#optimal solution using binary search
#Time complexity: O(nlogM+nlogn) where n is the num of elemetns and m is the max possible distance
#Space complexity: O(1) 
#need to add explanation for this


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)

        # Initialize binary search range
        low = 0
        high = nums[array_size - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            # Count pairs with distance <= mid
            count = self._count_pairs_with_max_distance(nums, mid)

            # Adjust binary search bounds based on count
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    # Count number of pairs with distance <= max_distance using a moving window
    def _count_pairs_with_max_distance(self, nums: List[int], max_distance: int) -> int:
        count = 0
        array_size = len(nums)
        left = 0

        for right in range(array_size):
            # Adjust the left pointer to maintain the window with distances <=
            # max_distance
            while nums[right] - nums[left] > max_distance:
                left += 1
            # Add the number of valid pairs ending at the current right index
            count += right - left
        return count