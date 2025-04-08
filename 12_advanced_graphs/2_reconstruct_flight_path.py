# You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.

# Each from_i and to_i consists of three uppercase English letters.

# Reconstruct the itinerary in order and return it.

# All of the tickets belong to someone who originally departed from "JFK". 
# Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

# If there are multiple valid flight paths, return the lexicographically smallest one.

# For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
# You may assume all the tickets form at least one valid flight path.

# Example 1:
# Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
# Output: ["JFK","BUF","HOU","SEA"]

# Example 2:
# Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
# Output: ["JFK","HOU","JFK","SEA","JFK"]
# Explanation: Another possible reconstruction is ["JFK","SEA","JFK","HOU","JFK"] but it is lexicographically larger.


#solution using adjacency list and dfs
# # time complexity: O(V * E) where V is number of vertices and E is number of edges
# # space complexity: O(V * E) where V is number of vertices and E is number of edges

#initialize the adj list with every source as a key and a empty list as a value
# #sort the tickets based on the source and destination
# #loop through the tickets and add the destination to the source in the adj list
# #initialize the result list with JFK as the first element since JFK is always the start

#call dfs on JFK
#return res. No validation needed because theres always one valid flight path

#the dfs function
#check that the length of the result is equal to the number of tickets + 1 to ensure all tickets are used
#check if the source is not in the adj list. If there's no where it can fly to, it's a bad path. return false

#create a temp list of the adj list for the source
#loop through the temp list with enumerate. We want to use the index to modify the adj list as we go. Thats why we use a temp

# #pop the index from the adj list and append it to the result
# #call dfs on the destination
# #if it returns true, return true
# #otherwise, undo the pop and append above with an insert and pop
# #return false outside the loop


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        #sort tickets based on pair, first index, then backup second index
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            #create temp so we can update the actual adj list while 
            #we iterate through it
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v): 
                    return True

                #undo the pop and append above
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res



#theres another solution using Hierholzer's algorithm with recursion that's more efficient
#but video went over the dfs adj list solution so idk
#time complexity: O(ElogE) Where E is the number of tickets (edges)
#space complexity: O(E)

#same start for this basically. Sort the tickets and make an adj list 
#initialize res as an empty list
#the dfs function
#takes in src
#while the src has a destination
#pop the destination from the adj list
#call dfs on the destination
#append the source to the result

#call dfs on JFK
#reverse the result and return it


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]

