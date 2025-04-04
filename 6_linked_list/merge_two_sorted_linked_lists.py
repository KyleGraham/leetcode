# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]



# optimal solution using iteration
# time complexity: O(n + m)
# space complexity: O(1)

#returning the head of the new list, so we initialize dummy to be returned and node as empty nodes

# while list1 and list2 are not empty
# if list1 value is less than list2 value, set node.next to list1 and move list1 to the next node
# else set node.next to list2 and move list2 to the next node
# move node

# set the last node to the remaining list1 or list2 as the loop will be broken if one of them is empty so always will have one empty after
#return dummy.next as its currently empty

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2

        return dummy.next