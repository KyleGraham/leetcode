# There is a long table with a line of plates and candles arranged on top of it. 
# You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the 
# substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles
# that are in the substring. A plate is considered between candles if there is at least one candle to its 
# left and at least one candle to its right in the substring.

# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". 
# The number of plates between candles in this substring is 2, 
# as each of the two plates has at least one candle in the substring to its left and right.
# Return an integer array answer where answer[i] is the answer to the ith query.

 

# Example 1:

# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.
# Example 2:

# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.

#solution using prefix
#time complexity:  O(n + q), where n is the length of the string and q is the number of queries.
#space complexity: O(n + q), where n is the length of the string and q is the number of queries.

# Precomputing Useful Information:

# candle_count: A prefix sum array that counts the number of candles up to each position.
# nearest_left_candle: For each position, stores the position of the nearest candle to its left.
# nearest_right_candle: For each position, stores the position of the nearest candle to its right.

# Processing Each Query:

# For a query [left, right], we first find the leftmost and rightmost candles within the range.
# If there aren't at least two candles in the range, we return 0 (as no plate can have candles on both sides).
# Otherwise, we calculate:

# Total elements between these candles
# Number of candles between these candles
# Therefore, plates between = total elements - candles between

#initialzie n as len(s)
#initialize candle_count as [0] * (n + 1)
#initialize nearest_left_candle as [-1] * n
#initialize nearest_right_candle as [n] * n
#initialize results as []

#loop through i in range n
#update candle_count[i + 1] as candle_count[i] + (1 if s[i] == '|' else 0)
#if s[i] == '|':
#update nearest_left_candle[i] as i
#elif i > 0:
#update nearest_left_candle[i] as nearest_left_candle[i - 1]

#loop through i in range n - 1, -1, -1
# if s[i] == '|':
# update nearest_right_candle[i] as i
#elif i < n - 1:
# update nearest_right_candle[i] as nearest_right_candle[i + 1]

#loop through left, right in each query
# find the leftmost and rightmost candles in the range
# left_candle = nearest_right_candle[left]
# right_candle = nearest_left_candle[right]
# if left_candle >= right_candle:
# results.append(0)
# continue
# total_elements = right_candle - left_candle - 1
# candles_between = candle_count[right_candle] - candle_count[left_candle + 1]
# plates_between = total_elements - candles_between
# results.append(plates_between)

#return results



class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Precompute useful information
        # 1. Count of candles up to each position
        candle_count = [0] * (n + 1)
        
        # 2. Position of the closest candle to the left for each position
        nearest_left_candle = [-1] * n
        
        # 3. Position of the closest candle to the right for each position
        nearest_right_candle = [n] * n
        
        # Fill candle counts and nearest left candle positions
        for i in range(n):
            # Update candle count prefix sum
            candle_count[i + 1] = candle_count[i] + (1 if s[i] == '|' else 0)
            
            # Update nearest left candle
            if s[i] == '|':
                nearest_left_candle[i] = i
            elif i > 0:
                nearest_left_candle[i] = nearest_left_candle[i - 1]
        
        # Fill nearest right candle positions (going right to left)
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nearest_right_candle[i] = i
            elif i < n - 1:
                nearest_right_candle[i] = nearest_right_candle[i + 1]
        
        # Process each query
        results = []
        for left, right in queries:
            # Find the leftmost and rightmost candles in the range
            left_candle = nearest_right_candle[left]
            right_candle = nearest_left_candle[right]
            
            # If we don't have at least 2 candles in the range
            if left_candle >= right_candle:
                results.append(0)
                continue
            
            # Total elements between the candles
            total_elements = right_candle - left_candle - 1
            
            # Number of candles between these positions
            candles_between = candle_count[right_candle] - candle_count[left_candle + 1]
            
            # Number of plates = total elements - candles
            plates_between = total_elements - candles_between
            
            results.append(plates_between)
        
        return results