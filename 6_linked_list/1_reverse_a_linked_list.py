# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

# optimal solution using iteration
 
# none -> 1 -> 2 -> 3 -> none

# none <- 1 <- 2 <- 3 <- none

# initialize prev to none since the prev value of the head is None
# initialize curr to head
# loop until it reaches end of linked list

# store current.next in temp since that link will break
# set current.next to prev
# set prev to current
# set current to temp
# return prev since that's the new head


# time complexity: O(n)
# space complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev