#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#Please implement encode and decode

# time complexity: O(n)
# space complexity: O(n + m)
# since # can be present, we use a number length and a delimter, # for us to read
# length can be multiple characters so we must use a while loop inside the while loop to read until the delimiter

class Solution:
    def encode(self, strs: List[str]) -> str:
        val = ""
        for value in strs:
            val += str(len(value)) + '#' + value
        return val

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            arr.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return arr
