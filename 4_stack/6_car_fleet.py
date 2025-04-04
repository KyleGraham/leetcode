# There are n cars traveling to the same destination on a one-lane highway.
# You are given two arrays of integers position and speed, both of length n.
# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.
# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
# Return the number of different car fleets that will arrive at the destination.
# Example 1:
# Input: target = 10, position = [1,4], speed = [3,2]
# Output: 1

#solution using stack
# time complexity O(n)
# space complexity O(n)
# create a list of pairs of position and speed 
# want the pairs to be in reverse sorted order, so the car in the front is the first car in the list
# iterate through the pairs, and calculate the time it takes to reach the target
# if the time is less than or equal to the last time in the stack, pop the last time from the stack
# else append the time to the stack

# zip is used here to create the list of pairs, you can also loop through i in len(position) and create the pairs
# using sorted in the loop is nice, and [::-1] is a nice trick to reverse the list

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)