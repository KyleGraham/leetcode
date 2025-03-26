#bucket sort
#Time complexity: O(n)
#Space complexity: O(n)
#creates a dictionary to store the frequency of each number
#creates a list of lists to store the numbers with the same frequency based on index, the index is the frequency of the number
#loops through the list in reverse and appends the numbers into a list until the length of the list is equal to k
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    frequency = [[] for i in range(len(nums) + 1)]

    for num in nums:
      count[num] = 1 + count.get(num, 0)
    
    for num, cnt in count.items():
      frequency[cnt].append(num)
    res = []
    for i in range(len(frequency) - 1, 0, -1):
      for num in frequency[i]:
        res.append(num)
        if len(res) == k:
          return res
