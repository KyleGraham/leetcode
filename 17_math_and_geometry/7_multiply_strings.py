# You are given two strings num1 and num2 that represent non-negative integers.

# Return the product of num1 and num2 in the form of a string.

# Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

# Note: You can not use any built-in library to convert the inputs directly into integers.

# Example 1:

# Input: num1 = "3", num2 = "4"

# Output: "12"
# Example 2:

# Input: num1 = "111", num2 = "222"

# Output: "24642"


#solution using multiplication
#time complexity: O(n * m) where n is len(num1) and m is len(num2)
#space complexity: O(n + m) where n is len(num1) and m is len(num2)

#says not to convert things to int, but that's only the given num1 and num2, since they can be numbers larger than can fit in an int

#check if either num1 or num2 is 0, if so return 0
#initialize res as a list of 0s with length of len(num1) + len(num2)
#reverse both strings
#loop through the digits in num1 and num2
#multiply the digits at the indexes after coverting them to int
#add the digit to the res at the index of i1 + i2
#add the carry to the next index
#do a mod on the res at the index of i1 + i2 to get the last digit just incase it's multi digit after the addition

#reverse the res
#initialize beg as 0
#while beg is less than the length of res and the value at beg is 0 #checking for leading zeroes
#increment beg by 1
#convert the res to a string array starting at the index of beginning
#join the array and return it

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1] #reverse both strings

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit #can be something like 12
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10 #handles the multi digit thing above
        res = res[::-1]
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)