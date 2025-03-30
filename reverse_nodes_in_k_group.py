

#optimal solution using iteration of linked list
#time complexity: O(n)
#space complexity: O(1)

#initialize dummy to be the beginning of the linked list, give it default 0 value, with head as the next
#initialize groupPrev to dummy, this will be the prev head of the group
#while loop on true
# get the kth node of the group, just increment the linked list k times
# check if kth is None, if so, break

#store the next value of the kth node as groupNext

#reverse the group with prev as kth.next and curr as groupPrev.next
#while curr is not groupNext, will loop through the first node of the group to the last node of the group
#store the next value of curr in tmp
#set curr.next to prev
#set prev to curr
#set curr to tmp

#hardest part here
#store the next value of groupPrev in tmp, this is the old head of the group and will be the new tail of the group
#set groupPrev.next to kth, linking the old head to the new head
#set groupPrev to tmp, this is the new head of the group
#return dummy.next as the new head of the linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            #reverse group
            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
