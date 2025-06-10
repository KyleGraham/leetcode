
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

#have to do this in place
#so we gather the total size of the group by incrementing the group variable if the next item is the same as the current until it changes or
#we reach the end

#check if group is bigger than 1, since groups of 1 get no number added
#then we conver the group from int to string
#modify the values from res to res + len(str_group) use len here for values like 12 with 2 digits
#change those values to list of str_group
#increment res by the len of str_group
#outsiude the if, increment i by group

#return res


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group = 1
            while (i + group < len(chars) and chars[i + group] == chars[i]):
                group += 1
            chars[res] = chars[i]
            res += 1
            if group > 1:
                str_group = str(group)
                chars[res:res+len(str_group)] = list(str_group) 
                res += len(str_group)
            i += group
        return res
            