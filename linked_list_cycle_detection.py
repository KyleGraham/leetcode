# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. 
# The tail node of the list will set it's next pointer to the index-th node. 
# If index = -1, then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.

# Example 1:
# Input: head = [1,2,3,4], index = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], index = -1
# Output: false


#optimal solution using tortoise and hare algorithm
#time complexity O(n)
#space complexity O(1)
# initialize slow and fast to head
# loop until fast and fast.next are not None

# no loop -> fast will reach a None and break out, return False
# with loop -> slow will eventually meet fast since they loop around, even if it takes a couple loops.abs
# returns True



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False