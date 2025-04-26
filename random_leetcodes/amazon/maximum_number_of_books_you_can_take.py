
# Solution Approach
# This solution uses dynamic programming with a monotonic stack. Here's how it works:
# 1. Key Insight
# If we select shelf i, we can't take all books from it if that would violate the constraint with shelf i+1. 
# This creates a pattern where the optimal number of books follows an arithmetic sequence.
# 2. The calculateSum Helper Function
# def calculateSum(l, r):
#     cnt = min(books[r], r - l + 1)
#     return (2 * books[r] - (cnt - 1)) * cnt // 2

# This calculates the maximum books we can take from a range of shelves [l, r]
# cnt is the number of shelves we can include (limited by books[r] or the range size)
# The formula uses arithmetic sequence sum: (first term + last term) × count / 2
# If we take x books from shelf r, we take x-1 from r-1, x-2 from r-2, etc.

# 3. Dynamic Programming with Stack

# dp[i] represents the maximum books we can take ending at shelf i
# stack helps us find the previous valid "breaking point"

# 4. Main Loop Step by Step
# For each shelf i:

# Clean the stack:
# while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
#     stack.pop()

# This removes indices that can't be used as previous breaking points
# The condition books[stack[-1]] - stack[-1] >= books[i] - i checks if the "rate of increase" breaks our constraint


# Calculate dp[i]:
# if not stack:
#     dp[i] = calculateSum(0, i)
# else:
#     j = stack[-1]
#     dp[i] = dp[j] + calculateSum(j + 1, i)

# If the stack is empty, we calculate from the beginning
# Otherwise, we use the last valid breaking point (j) and add the new segment


# Update the stack:
# stack.append(i)

# Add the current index to the stack for future calculations



# 5. Return the Result
# return max(dp)

# The maximum value in the dp array is our answer

# Visual Example
# For books = [8,5,2,7,9]:

# i=0: dp[0] = 8 (take 8 books from shelf 0), stack = [0]
# i=1: dp[1] = 13 (take 4 from shelf 0, 5 from shelf 1), stack = [1]
# i=2: dp[2] = 14 (take 1 from shelf 0, 2 from shelf 1, 2 from shelf 2), stack = [2]
# i=3: dp[3] = 16 (take 1+2+6+7=16), stack = [3]
# i=4: dp[4] = 19 (take 1+2+7+9=19), stack = [4]

# Final answer: max(dp) = 19
# This solution efficiently handles the constraint of taking strictly fewer books from left shelves compared to right shelves 
# by using dynamic programming and a monotonic stack to find optimal breaking points.



class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        # Helper function to calculate the sum of books in a given range [l, r]
        def calculateSum(l, r):
            cnt = min(books[r], r - l + 1)
            return (2 * books[r] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * n

        for i in range(n):
            # While we cannot push i, we pop from the stack
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            # Compute dp[i]
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)

            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum element in the dp array
        return max(dp)