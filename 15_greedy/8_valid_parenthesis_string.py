# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# A string is valid if it follows all of the following rules:

# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

# Example 1:
# Input: s = "((**)"
# Output: true
# Explanation: One of the '*' could be a ')' and the other could be an empty string.

# Example 2:
# Input: s = "(((*)"
# Output: false

#greedy solution
#time complexity: O(n)
#space complexity: O(1)

#essentially, we want to keep track of a leftMin and a leftMax, to keep track of any wildcards
#essentially, when we hit a wildcard, we can use it to subtract from a parenthesis, or add one, or do nothing with an empty string

#initialize leftMin and leftMax to 0

#loop through the string
#check if the character is a left parenthesis, then increment both leftMin and leftMax by 1
#check if the character is a right parenthesis, then decrement both leftMin and leftMax by 1
#check if the character is a wildcard, then decrement leftMin by 1 and increment leftMax by 1
#check if leftMax is less than 0, then return False
#check if leftMin is less than 0, then set leftMin to 0
#return True if leftMin is equal to 0, else False


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0