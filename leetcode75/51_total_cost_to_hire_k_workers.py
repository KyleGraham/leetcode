# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. 
# Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, 
# we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but 
# they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. 
# Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.

 

# Example 1:

# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. 
# The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8].
#  The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. 
# The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
# Example 2:

# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. 
# The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. 
# Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. 
# The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates.
#  We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.
 

# Constraints:

# 1 <= costs.length <= 105 
# 1 <= costs[i] <= 105
# 1 <= k, candidates <= costs.length

#solution using priority queues
# m = candidates
# time complexity: O((k + m) * log m)
# space complexity: O(m)

# Algorithm
# Initialize two priority queues head_workers and tail_workers that store the first m workers and the last m workers, 
# where the worker with the lowest cost has the highest priority.

# Set up two pointers next_head = m, next_tail = n - m - 1 indicating the next worker to be added to two queues.

# Compare the top workers in both queues, and hire the one with the lowest cost, if both workers have the same cost,
# hire the worker from head_workers. Add the cost of this worker to the total cost.

# If next_head <= next_tail, we need to fill the queue with one worker:

# If the hired worker is from head_workers, we add the worker costs[next_head] to it and increment next_head by 1.
# If the hired worker is from tail_workers, we add the worker costs[tail_head] to it and decrement tail_head by 1.
# Otherwise, skip this step.

# Repeat steps 3 and 4 k times.

# Return the total cost of all the hired workers.


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)
        
        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates 

        for _ in range(k): 
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]: 
                answer += heappop(head_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail: 
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else: 
                answer += heappop(tail_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:  
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1
                    
        return answer