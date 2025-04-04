# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

#solution using one stack
# time complexity O(n)
# space complexity O(n)
# initialize list of possible operators to check for
# initialize stack, if any number is found, it will be pushed to the stack (convert to int from str)
# if an operator is found, pop the last two numbers from the stack and apply the operator
# push the result back to the stack
# else push number to stack
# return the last number in the stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for item in tokens:
            if item in operators:
                right = stack.pop()
                left = stack.pop()
                if item == '+':
                    left = left + right
                elif item == '-':
                    left = left - right
                elif item == '*':
                    left = left * right
                else:
                    left = int(left / right)
                stack.append(left)
            else:
                stack.append(int(item))
        
        return stack.pop()