# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
# If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
# Example 1:
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]
# Example 2:
# Input: temperatures = [22,21,20]
# Output: [0,0,0]

# solution using stack
# time complexity O(n)
# space complexity O(n)

#default results array to 0 with len of temperatures
# initialize stack, this will hold an array of the temperature and index
# iterate through the temperatures
# while the stack is not empty and the current temperature is greater than the last temperature in the stack
# pop the last temperature and index from the stack and set the result at the index to the difference between the current index and the popped index
# append the current temperature and index to the stack
# return the results array

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res 