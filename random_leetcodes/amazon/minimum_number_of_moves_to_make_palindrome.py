# You are given a string s consisting only of lowercase English letters.

# In one move, you can select any two adjacent characters of s and swap them.

# Return the minimum number of moves needed to make s a palindrome.

# Note that the input will be generated such that s can always be converted to a palindrome.

#greedy solution
# Time Complexity: O(n²)
# Space Complexity: O(n)


# The code converts the string to a list for easier character manipulation
# It processes the string from both ends (like forming a palindrome)
# For each iteration:

  # It looks for the first occurrence of the last character
  # If that character is the last one itself (unique character), it needs i/2 swaps to position it in the middle
  # Otherwise, it needs i swaps to bring the matching character to the front
  # It removes both matched characters and continues


class Solution:
    def minMovesToMakePalindrome(self, s):
        s = list(s)  
        res = 0      
        
        while s:     
            i = s.index(s[-1])  # Find the index of the first occurrence of the last character
            
            # Case: Last character is unique (it belongs in the middle of palindrome)
            if i == len(s) - 1:
                # For a single character that needs to go to the middle,
                # we need i/2 swaps to get it to the middle position
                res += i // 2
            
            # Case: Match found earlier in the string
            else:
                # Add the number of swaps needed to bring this character to the front
                res += i
                # Remove the matched character
                s.pop(i)
            
            # Remove the last character we just processed
            s.pop()
        
        return res