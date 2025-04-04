# You are given the head of a linked list of length n. 
# Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
# Create a deep copy of the list.
# The deep copy should consist of exactly n new nodes, each including:
# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.
# Return the head of the copied linked list.
# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
# Output: [[3,null],[7,3],[4,0],[5,1]]

# Example 2:
# Input: head = [[1,null],[2,2],[3,2]]
# Output: [[1,null],[2,2],[3,2]]


#two pass solution using hash map
#time complexity: O(n)
#space complexity: O(n)

#main issue with this problem is that when we deep copy a node, the random pointer can point to a node that we have not seen yet in the loop
#create a hash map, default the value to {None:None} since if cur.random is None, we want to return None
#loop through linked list and create a copy of each node
#store the original node as the key and the copy as the value
#loop through linked list again
# initialize copy as the current value
# set copy.next to the copy of the next value
# set copy.random to the copy of the random value
# return the copy of the head


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None} # for if cur.random is None
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]