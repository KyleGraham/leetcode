# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


#solution using stack
#time complexity: O(maxK * n) k = max val of ints, n is the length of given string
#space complexity: O(m + n) - for stack


#essentially loop through string and handle different logic for each character
#for [, we add the cur string and num to the stack and reset their values after
#for ], we pop the num and string from the stack, then set curString to the stack value + num * curString

#if c.isdigit(), we do curNum = curNum * 10 + int(c). This handles multi digit numbers
# if c is 1,    curNum = 1
# then c is 2,  curNum = 12
# then c is 3,  curNum = 123

#else c is a non digit char, add it to res
#return res

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        res = ''
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(curNum)
                res = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                res = prevString + num * res
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                res += c
        return res