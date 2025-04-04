#Better solution using basically merge sort
#time complexity: O(nlog(n))
#space complexity: O(k) where k is the number of linked lists


#using that same merge two lists function from before
#do a while loop while the length of the lists is greater than 1
# initialize a merged list, this will end up being half the length of the original list
# do a for loop while incrementing by 2
# check that the next index is not out of bounds, default to None if so
#merge the two lists
# set the lists to the merged list

#return the first element of the list since it will be the only element left


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            lists = mergedList
        return lists[0]

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




#essentially, if you can merge 2 sorted linked lists, you can merge k sorted linked lists

# initialise a result node with a value of negative infinity, this will be the head of the new linked list
# iterate through the list of linked lists
# merge the result node with the current linked list
# return the result node.next as the head of the new linked list

# time complexity: O(n * m) where n is the number of linked lists and m is the number of nodes in each linked list
# space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode((float('-infinity')))
        for list in lists:
            res = self.mergeTwoLists(res, list)
        return res.next

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