# You are given the beginning of a linked list head, and an integer n.
# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:
# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]

# Example 2:
# Input: head = [5], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 2
# Output: [2]

# solution using 2 pointers
# time complexity: O(n)
# space complexity: O(1)

#add a dummy node to the beginning of the linked list with dummy = ListNode(0, head)
#initialize the left pointer as the dummy
#initialize the right pointer as the head

#move the right pointer over n times, so the left pointer is n steps behind the right pointer the val we want to remove

#traverse the list with the right pointer with a while loop
#after, the right pointer is at the end of the linked list, and the left pointer is n items behind the end
#delete the value
#return the dummy value.next to get the head
#returning the dummy helps in edge cases like only one val


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next