# You are given the head of a singly linked-list.
# The positions of a linked list of length = 7 for example, can intially be represented as:
# [0, 1, 2, 3, 4, 5, 6]
# Reorder the nodes of the linked list to be in the following order:
# [0, 6, 1, 5, 2, 4, 3]
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
# [0, n-1, 1, n-2, 2, n-3, ...]
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:
# Input: head = [2,4,6,8]
# Output: [2,8,4,6]

# Example 2:
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]

# use fast and slow pointer. Slow will hit halfway point, fast will hit the end
# reverse the second half of the linked list
# can use tortoise and hare algorithm to find the halfway point!!!!!!


# time complexity: O(n)
# space complexity: O(1)

#use tortoise and hare algorithm to find the halfway point
#start second list on slow.next 
#reverse the second list

#merge the two lists
# first pointer goes to head
# second pointer goes to prev, the first item in the reversed list
# while loop on second because it can be shorter
# create temporary variables to store the next values of both heads
# set the next value of first to second
# set the next value of second to the temporary variable of the first node
# move the first and second pointers to the next nodes using the temps



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        #find middle point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two halfs
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2