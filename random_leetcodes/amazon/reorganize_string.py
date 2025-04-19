# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""

#solution using priority queue (max heap)
#time complexity: O(n log k) where n is the length of the string and k is the number of unique characters, arguably O(n) since k is at most 26
#space complexity: O(k)

# Given a string s, rearrange the characters of s so that no two adjacent characters are equal.

#we use a priority queue based on the most frequent character as the priority
#we use a max heap to store the character and its count (remember negative count)
# pq = [(-count, char) for char, count in Counter(s).items()]
# heapify(pq) to create the heap
#initialize res as the result array
#while pq:
#pop the most frequent character from the heap
#check if the last character in res is not equal to the current character res[-1] to get last character in the list
# if so, append the current character to res
#check if the counter + 1 is not equal to zero
# if so, push the current character back to the heap with count + 1

# if the last character is equal to the current character, we need to pop the next most frequent character
#pop the next most frequent character from the heap
#append the next character to res
#check if the counter + 1 is not equal to zero
# if so, push the next character back to the heap with count + 1
#push the first character back to the heap

#finally return the result as a string by joining the list res


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []

        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)

        while pq:
            count_first, char_first = heappop(pq)
            if not res or char_first != res[-1]:
                res.append(char_first)
                if count_first + 1 != 0:
                    heappush(pq, (count_first + 1, char_first))
            else:
                if not pq: return ''
                count_second, char_second = heappop(pq)
                res.append(char_second)
                if count_second + 1 != 0:
                    heappush(pq, (count_second + 1, char_second))
                heappush(pq, (count_first, char_first))

        return ''.join(res)
