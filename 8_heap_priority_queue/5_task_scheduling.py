# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:
# Input: tasks = ["X","X","Y","Y"], n = 2
# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:
# Input: tasks = ["A","A","A","B","C"], n = 3
# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.


#optimum solution using a max heap, a count, and also a queue
#time complexity (O(m)) where m is the number of tasks
#space complexity (O(1)) since at most 26 characters

#uses a count to get the count of each task
#uses a max heap sort the tasks in the count of each task in descending order. They're negatives cuz python
#uses a queue to store the tasks that are not ready to be executed. Store the count of tasks and the index that it can be executed

#loop while the max heap or the queue is not empty
#increment i
#if the max heap is not empty
#pop the max heap
#decrement the count of the task
#if the count is not 0, add it to the queue with the index of i plus n

#if the queue is not empty and the index of the first element in the queue is equal to i
#push the element back to the max heap for execution

#any misses on either if statement will increment i and basically be an idle

#return i

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        i = 0
        q = deque()

        while maxHeap or q:
            i += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, i + n])
            if q and q[0][1] == i:
                heapq.heappush(maxHeap, q.popleft()[0])

        return i