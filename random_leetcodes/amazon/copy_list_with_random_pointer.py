#repeat from neetcode



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
        #intialize this as None just incase a random pointer is to None
        #since the random pointer can point anywhere, you have to 
        #initialize a hash and put all the nodes in the hash
        #that way when you loop through the nodes again, you can
        #properly make a copy with access to all the nodes
        hash = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            hash[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next
        return hash[head]

        