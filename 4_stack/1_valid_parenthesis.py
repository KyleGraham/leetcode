#You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# optimal solution using stack
# time complexity: O(n)
# space complexity: O(n)
# uses a stack to keep track of the open brackets
# use hash to keep the closing brackets and the expected opening bracket
# loops through the string
# if the character is a closing bracket, checks if the stack is empty, returns false if it is
# pops the last value from the stack and checks if it is the expected opening bracket
# returns false if it is not
# returns false if the stack is not empty at the end
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketHash = {'}': '{', ')': '(', ']': '['}
        for c in s:
            if c in bracketHash.keys():
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if not open == bracketHash[c]:
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True