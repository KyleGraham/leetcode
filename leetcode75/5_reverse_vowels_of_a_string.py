

#one pass solution using two pointers
#instead of using lower(), just add the captial vowels to the array
#also no need for temp when using python, can do it in just one line
#items[r], items[l] = items[l], items[r]

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
        l = 0
        r = len(s) - 1
        items = list(s)
        while l < r:
            if items[l] not in vowels:
                l += 1
            if items[r] not in vowels:
                r -= 1
            if items[r] in vowels and items[l] in vowels:
                items[r], items[l] = items[l], items[r]
                l += 1
                r -= 1
        return "".join(items)
