# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
# Example 1:
# Input: n = 1
# Output: ["()"]
# Example 2:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]



#solution using recusion and a stack
# time complexity O(4n/log(n))
# space complexity O(n)
#keep track of open and closed parentheses
# only add open parentheses if open < n
# only add a closing parentheses if closed < open
# valid IFF open == closed == n
# add the result to the list
# after calling the recusion, must pop the last item in the stack to keep state correct

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IFF open == closed == n
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res    