# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"



#solution using an array
#time complexity O(n)
#space complexity O(n)

#initializes rows as an array of strings with the length of num rows

#instead of doing the zig zag pattern and converting it, this fills the rows with the actual output
#if the index reaches the start or end of 0-numRows, the bool reverses
#if backward, the index subtracts one, else it adds one
#then return "".join(rows)


# s =
# "PAYPALISHIRING"
# numRows =
# 4

#character, index, backward
# P 0 True
# A 1 False
# Y 2 False
# P 3 False
# A 2 True
# L 1 True
# I 0 True
# S 1 False
# H 2 False
# I 3 False
# R 2 True
# I 1 True
# N 0 True
# G 1 False

#rows
#['PIN', 'ALSIG', 'YAHR', 'PI']
 
#output
#"PINALSIGYAHRPI"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows
        backward = True
        index = 0
        for char in s:
            rows[index] += char
            if index == 0 or index == numRows - 1:
                backward = not backward
            if backward:
                index -= 1
            else:
                index += 1
        return "".join(rows)