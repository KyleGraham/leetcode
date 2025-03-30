# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Return the sum of the two numbers as a linked list.

# Example 1:
# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.

# Example 2:
# Input: l1 = [9], l2 = [9]
# Output: [8,1]

# time complexity: O(n + m)
# space complexity: O(1)

#important, linked list comes reversed, so first value is the most right digit, which you add first anyways
#also important, you have to worry about carry like with addition, so 7 + 8 = 15, so you have to carry the 1
# carry can exist after the loop, so you have to check if carry > 0 and add a new node

# create a dummy node and point a variable at that dummy node so we dont modify it
# create a carry variable to store the carry
# do a while loop on if there's value in l1 or l2
# get the value of l1 and l2, if they exist, else 0
# add the values and carry
# check the carry by floor dividing by 10
# get the value by modding by 10
# create a new node with the value
# increment the new node and also l1/l2, check if they exist

#after the loop, check the carry and add a new node if it exists
# return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #new digit
            val = v1 + v2 + carry
            #check if carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next