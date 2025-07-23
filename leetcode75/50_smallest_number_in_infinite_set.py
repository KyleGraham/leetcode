# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain 
# all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set,
# if it is not already in the infinite set.
 

# Example 1:

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", 
#  "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, 
# and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

# Constraints:

# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.




#solution with sorted set
# Time complexity: O((m+n)⋅logn)
# Space complexity: O(n)


# Initialize some variables:

# addedIntegers, a sorted set to store added numbers in increasing order.
# currentInteger, an integer variable initialized to 1, 
# used to denote the current minimum value number in the set of all positive numbers.
# In the popSmallest() method:

# If we have any element present in the sorted-set addedIntegers, 
# then the minimum number present in it is the answer. We remove it from the set.
# Otherwise, the number denoted by currentInteger is our answer, 
# and then we increment currentInteger by 1 which denotes we removed 
# the previous number and moved to the next number in our set of all positive numbers.
# In the end, we return answer.
# In the addBack(num) method:

# If the 'num' is already present in our set, then we return.
# Otherwise, we push it in the sorted-set addedIntegers.

class SmallestInfiniteSet:

    def __init__(self):
        self.added_integers = SortedSet()
        self.current_integer = 1
        

    def popSmallest(self) -> int:
        # If there are numbers in the sorted-set, 
        # top element is lowest among all the available numbers.
        if len(self.added_integers):
            answer = self.added_integers[0]
            self.added_integers.discard(answer)
        # Otherwise, the smallest number of large positive set 
        # denoted by 'current_integer' is the answer.
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer
        

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.added_integers:
            return
        # We push 'num' in the sorted-set if it isn't already present.
        self.added_integers.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)