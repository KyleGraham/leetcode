#brute force solution using hash maps similar to valid_anagram solution
#time complexity: O(M * nlog(n)
# space complexity: O(n * M)
class Solution1:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      if len(strs) == 1:
          return [strs]
      if len(strs) == 0:
          return [[""]]
      group_anagrams = []
      hash_groups = []
      for i, s in enumerate(strs):
          temp_hash = {}
          for j in range(len(s)):
              if s[j] in temp_hash:
                  temp_hash[s[j]] += 1
              else:
                  temp_hash[s[j]] = 1
          if temp_hash in hash_groups:
              if group_anagrams[hash_groups.index(temp_hash)]:
                  group_anagrams[hash_groups.index(temp_hash)].append(s)
              else:
                  group_anagrams.append(s)
          else:
              group_anagrams.append([s])
              hash_groups.append(temp_hash)
      return group_anagrams

# Optimized solution using hash maps, specifically using defaultDict that allows you to set key that does not exist, requires from collections import defaultdict
# time complexity: O(n * m)
# space complexity: O(n * m)
# loops through each string in the list of strings
# creates a count array of 26 elements, initializes all elements to 0
# uses the unicode of the char minus the unicode of 'a' to get the index of the character in the count array
# increments the count of the character in the count array
# converts the count array to a tuple and appends the string to the dictionary using the tuple as the key
# returns the values of the dictionary
class Solution2:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list)
      for s in strs:
          count = [0] * 26
          for c in s:
              count[ord(c) - ord('a')] += 1
          res[tuple(count)].append(s)
      return list(res.values())
 


#other solution using hashmap and defaultDict with sorting
#time complexity: O(n * mlog(m))
#space complexity: O(n * m)
#cleaner version of my brute force
# sorts the string and uses the sorted string as the key in the dictionary
# appends the string to the dictionary using the sorted string as the key
# returns the values of the dictionary

class Solution3:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list)
      for s in strs:
          sortedS = ''.join(sorted(s))
          res[sortedS].append(s)
      return list(res.values())