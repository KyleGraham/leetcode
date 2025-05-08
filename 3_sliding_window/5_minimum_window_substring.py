# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
#If such a substring does not exist, return an empty string "".

#leetcode solution
# Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T.
# In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. 
# ∣T∣ represents the length of string T.

# Space Complexity: O(∣S∣+∣T∣). ∣S∣ when the window size is equal to the entire string S. ∣T∣ when T has all unique characters.

#1 We start with two pointers, left and right initially pointing to the first element of the string S.

#2 We use the right pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of T.

#3 Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.

#4 If the window is not desirable any more, we repeat step2 onwards.

#comments in code explain everything else


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if (
                character in dict_t
                and window_counts[character] == dict_t[character]
            ):
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if (
                    character in dict_t
                    and window_counts[character] < dict_t[character]
                ):
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

#without comments
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if (character in dict_t and window_counts[character] == dict_t[character]):
                formed += 1

            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if (character in dict_t and window_counts[character] < dict_t[character]):
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]







# optimum solution using sliding window
# time complexity: O(n)
# space complexity: O(n)
# calculate the character count of t, the shorter string or target string
# uses the number of unique characters in t as the need variable
# we then can check how many characters in the substring that match in the have var
# we then loop through the string and increment the count of the character in the substring
# if the count of the character in the substring is equal to the count of the character in t, increment the have variable
# if the have variable is equal to the need variable, we have found a substring that contains all the characters in t
#once the have and need match, document the substring and length if it's smaller than the current length
#then increment the L variable, if the have and need still match, document the substring, if they do not, increment the R variable
#return the substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        t_count = {}
        s_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        need = len(t_count)
        have = 0
        res = [-1, -1]
        res_len = float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] = 1 + s_count.get(c, 0)
            if c in t_count and s_count[c] == t_count[c]:
                have += 1
            while have == need:
                if res_len > r - l + 1:
                    res_len = (r - l + 1)
                    res = [l, r]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1 
        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ""