# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]



#time complexity O(n)
#space complexity O(1)

#basically deal with the odds and evens as seperate linked lists, while keeping track as the first even to add it to the end of the odd list
#start odd at the first
#start even at the second
#while even and even.next

#set odd.next to odd.next.next, basically setting the next value in odd to the next odd value
#same with even basically
#increment odd and even by 1, setting it to the next odd or even value

#set odd.next to even_head
#return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head