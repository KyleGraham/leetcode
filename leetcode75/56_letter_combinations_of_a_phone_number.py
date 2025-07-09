
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].



#solution using backtracking
#time complexity: O(4&n * n)
#space complexity: O(n)



#backtracking pattern basically
# cur.append(digit.charAt(i));
# DFS(digits, index + 1, myMap, cur, myList);
# cur.deleteCharAt(cur.length() - 1);


# in here its
#  path.append(letter)
# backtrack(index + 1, path)
# path.pop()

# Algorithm

# As mentioned previously, we need to lock-in letters when we generate new letters. 
# The easiest way to save state like this is to use recursion. Our algorithm will be as follows:

# If the input is empty, return an empty array.

# Initialize a data structure (e.g. a hash map) that maps digits to their letters, for example, mapping "6" to "m", "n", and "o".

# Use a backtracking function to generate all possible combinations.

# The function should take 2 primary inputs: the current combination of letters we have, path, and the index we are currently checking.
# As a base case, if our current combination of letters is the same length as the input digits, that means we have a complete combination. 
# Therefore, add it to our answer, and backtrack.
# Otherwise, get all the letters that correspond with the current digit we are looking at, digits[index].
# Loop through these letters. For each letter, add the letter to our current path, and call backtrack again, but move on to the next digit by incrementing index by 1.
# Make sure to remove the letter from path once finished with it.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations