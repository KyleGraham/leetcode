# Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. 
# Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

# When you get an instruction 'A', your car does the following:
# position += speed
# speed *= 2
# When you get an instruction 'R', your car does the following:
# If your speed is positive then speed = -1
# otherwise speed = 1
# Your position stays the same.
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

# Given a target position target, return the length of the shortest sequence of instructions to get there.

 
# Example 1:

# Input: target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0 --> 1 --> 3.
# Example 2:

# Input: target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.


#solution using bfs
#time complexity: O(n)
#space complexity: O(n)

#initialize a q
#initialize a result variable to infinity

#while the q is not empty
#pop the leftmost element of the q, which is the num steps, position, and velocity
#check if the position is equal to the target
#update the result variable to the minimum of the result and steps
#check if the steps are greater than the result
#continue if so
#append the q with steps + 1, position + velocity, and velocity * 2

#check if position + velocity > target and velocity > 0 or position + velocity < target and velocity < 0
#append the q with steps + 1, position, and -1 if velocity > 0 else 1
#return the result variable



from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        q = deque([(0, 0, 1)])
        result = float("inf")
        
        while q:
            # num steps, position, velocity
            steps, pos, vel = q.popleft()
            if pos == target:
                result = min(result, steps)
            
            if steps > result:
                continue

            #2. Always consider moving the car in the direction it is already going
            q.append((steps+1, pos+vel, vel*2))
            #3. Only consider changing the direction of the car if one of the following conditions is true
            #   i.  The car is driving away from the target.
            #   ii. The car will pass the target in the next move.  
            if (pos+vel > target and vel > 0) or (pos+vel < target and vel < 0):
                q.append((steps+1, pos, -1 if vel > 0 else 1))
                
        return result