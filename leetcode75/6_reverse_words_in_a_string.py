
#one interviewers prob wont like
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


#one pass solution
#should be around O(n) time complexity

#some test cases have wierd spacing between words, thats why you gotta check if word before adding to result

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip()
        res = ""
        r = len(s) - 1
        while r >= 0:
            end = r
            while r >= 0 and s[r] != ' ':
                r -= 1
            start = r
            word = s[start+1:end+1]
            if word:
                res += word
                if not r == -1:
                    res += " "
            r -= 1
        return res