
#bellman ford algorithm - on benefit over dijkstra is that it can handle negative weights
#this isnt necessary for this problem at all, but fun fact to know

#trying to find the minimum cost to get to a node 
#doing k + 1 stops, since k is max number of stops not including the starting and destination node
#k + 1 is how many bfs layers we're doing basically
#must use temp array to hold the prices because otherwise it will check multiple stops in one stop
#A -> B -> C. have flight that goes from A -> c and A -> B -> C
#without the temp, the algo can read the actual cost of getting to B while reading the cost to get from b to c
#this shouldn't be possible. But since the value was directly added to the array, it's there and can read it
#essentially calculating for 1 stop when 1 stop is not allowed

#solution using bellman ford algorithm
#time complexity O(n + (m * k)) where n is the number of nodes, m is the number of edges and k is the number of stops
#space complexity O(n) where n is the number of nodes

# #initialize the prices as a list of infinity with len of n
# #set the source to 0
# #loop through the number of stops (k + 1)
# #initialize a temp prices list as a copy of the prices list
# #loop through the flights for s, d, p in flights: #source, destination, price
# #check if the price of the source is infinity
# # if so, continue since we can't get to the source
# #check if the price of the source + price is less than the temp price of the destination
# # if so, set the temp price of the destination to the source price + price
# #set the prices to the temp prices
# #outside the loop, check if the price of the destination is infinity
# # if so, return -1 since we can't get to the destination
# #otherwise, return the price of the destination


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights: #source, destination, price
                if prices[s] == float("infinity"):
                    continue
                if prices[s] + p  < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("infinity") else prices[dst]





#Solution using dijkstra's algorithm
#time complexity ((n + m) * k) where n is the number of nodes, m is the number of edges and k is the number of stops
#space complexity O(n + m) where n is the number of nodes and m is the number of edges

#initialize a constant INF as infinity
#initialize an adjacency list as a list of empty lists, the index will be the key basically since its a list




class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)]
        for s, d, p in flights:
            adj[s].append([d, p])
        
        dist[src][0] = 0
        minHeap = [(0, src, -1)] # cost, node, stops
        while len(minHeap):
            p, s, d
            p, node, d = heapq.heappop(minHeap)
            if dst == s: return p
            if d == k or dist[s][d + 1] < p:
                continue
            for nei, w in adj[s]:
                nextP = p + w
                nextD = 1 + d
                if dist[nei][nextD + 1] > nextP:
                    dist[nei][nextD + 1] = nextP
                    heapq.heappush(minHeap, (nextP, nei, nextD))

        return -1



