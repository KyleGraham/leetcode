

#solution using prefix sum
#time complexity: O(n)
#space complexity: O(n)

#if I get asked this I'm screwed



class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        mod = 1_000_000_007
        
        # for each strength[i], find [i - l + 1 to i + r - 1 inclusive]
        # s.t. strength[i] is the leftmost occurence of minimum
        len_l = [0] * n 
        len_r = [0] * n 
        stk = []
        
        for i in range(n - 1, -1, -1):
            while stk and strength[stk[-1]] >= strength[i]:
                j = stk.pop()
                len_l[j] = j - i
            stk.append(i)
        for j in stk:
            len_l[j] = j + 1
        
        for i in range(n):
            while stk and strength[stk[-1]] > strength[i]:
                j = stk.pop()
                len_r[j] = i - j
            stk.append(i)
        for j in stk:
            len_r[j] = n - j
			
        # prefix sum of prefix sum
        psps = list(accumulate(accumulate(strength))) + [0]
        
        ans = 0
        for i in range(n):
            L = len_l[i]
            R = len_r[i]
            total_R = (psps[i + R - 1] - psps[i - 1]) * L
            total_L = (psps[i - 1] - psps[max(-1, i - L - 1)]) * R
            ans = (ans + strength[i] * (total_R - total_L)) % mod
        return ans