

#solution using dfs
#time complexity O(n * m) where n = # equations and m = # queries
#space complexity O(n)

#basically if a/b = 2, then b/a = 1/2
# and if a/b = 2 and b/c = 3 then a/c = 6 since a/c = a/b * a/c
#so we determine these by a graph basically?
#idk if this gets asked i'm prob boned
#  -> a/b = 2      -> b/c = 3
# a              b             c
#  <- b/a = 1/2   <- c/b = 1/3


#create the graph 
#  # Step 1). build the graph from the equations
#         for (dividend, divisor), value in zip(equations, values):
#             # add nodes and two edges into the graph
#             graph[dividend][divisor] = value
#             graph[divisor][dividend] = 1 / value



 # Step 2). Evaluate each query via backtracking (DFS)
        # #  by verifying if there exists a path from dividend to divisor
        # results = []
        # for dividend, divisor in queries:
        #     if dividend not in graph or divisor not in graph:
        #         # case 1): either node does not exist
        #         ret = -1.0
        #     elif dividend == divisor:
        #         # case 2): origin and destination are the same node
        #         ret = 1.0
        #     else:
        #         visited = set()
        #         ret = backtrack_evaluate(dividend, divisor, 1, visited)
        #     results.append(ret)


#the backtrack dfs equation
#  def backtrack_evaluate(curr_node, target_node, acc_product, visited):
#             visited.add(curr_node)
#             ret = -1.0
#             neighbors = graph[curr_node]
#             if target_node in neighbors:
#                 ret = acc_product * neighbors[target_node]
#             else:
#                 for neighbor, value in neighbors.items():
#                     if neighbor in visited:
#                         continue
#                     ret = backtrack_evaluate(
#                         neighbor, target_node, acc_product * value, visited)
#                     if ret != -1.0:
#                         break
#             visited.remove(curr_node)
#             return ret




class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results
        