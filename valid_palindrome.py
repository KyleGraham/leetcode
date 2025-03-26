#solution using two pointers
#time complexity: O(n)
#space complexity: O(1)
#remove any non alphanumeric characters and convert to lowercase
# loop through the string starting from the front and back and check that the characters are the same
# if they are not, return False
#if not using isalnum, you can make a function for it like this
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #             ord('a') <= ord(c) <= ord('z') or 
    #             ord('0') <= ord(c) <= ord('9'))
#basically checks that the ascii of the character is within range of the capital, lowercase, or number ascii values

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        for i in range(len(newStr)):
            j = len(newStr) - 1 - i
            if newStr[i] != newStr[j]:
                return False
        return True