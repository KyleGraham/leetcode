# You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

# You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

# Return true if it's possible to rearrange the cards in this way, otherwise, return false.

# Example 1:

# Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

# Output: true
# Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

# Example 2:

# Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

# Output: false
# Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.

#greedy solution using a hash map and a min heap
#time complexity: O(n log n)
#space complexity: O(n)

#first we check if len of hand is divisible by groupSize
# if not, return false

#initialize a counter to count the number of times each number appears in hand
#the commented out code below it is equivalent basically. just returns a hashmap

#initialize minH as a list of the keys in count
#heapify minH
#while minH is not empty
# get the first element in minH must minH[0]
# for each number from first to first + groupSize
# check if the number is in count
# if not, return false
# decrement the count of the number in count
# if the count is 0, 
# check if the number is not equal to minH[0]
#if we're popping a val that isn't equivalent to the count that just went to 0, return false
# pop the minH
# return true at the end




class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        # count = {}
        # for n in hand:
        #     count[n] = 1 + count.get(n, 0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True