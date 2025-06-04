# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks,
# and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

 

# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Example 2:

# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

#solution using DFS
#time complexity O(N + E) where n = num rooms and e = total num of keys
#space complexity O(N)

#initialize a memoization array as false to the length of the room
#set the first room as true

#do dfs function
#set the mem of the room to True
#for the keys in the room
#check if they're not set true in mem
#if not, call dfs on the room

#call dfs on 0
#then return true if every val in the mem array == True



class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        mem = [False] * len(rooms)
        mem[0] = True

        def dfs(room):
            mem[room] = True
            for key in rooms[room]:
                if not mem[key]:
                    dfs(key)
        dfs(0)
        for room in mem:
            if not room:
                return False
        return True
