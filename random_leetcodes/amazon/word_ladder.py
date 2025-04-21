
# You are given two words, beginWord and endWord, and also a list of words wordList. 
# All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

# Your goal is to transform beginWord into endWord by following the rules:

# You may transform beginWord to any word within wordList, 
# provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
# You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
# Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
# Output: 4
# Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

# Example 2:
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]
# Output: 0
# Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList.



#solution using adjacency list and bfs
#time complexity O(m^2 * n) where n is the number of words and m is the length of the word
#space complexity O(m^2 * n) where n is the number of words and m is the length of the word

#so I wanted to just go through every character of a word and compare it to another word to check if they have n-1 same chars
#but on words like miss and most, it should return 2, but because of the 2 s characters, it returns 3
#so we have to basically create a pattern for each word using a * as a wildcard
#so miss would be *iss, m*ss, mi*s, mis*
#and most would be *ost, m*st, mo*t, mos*

#check if the endword is not in the word list
# if so, return 0 since we can't reach it
#initialize a defaultdict of lists
#add the begin word to the word list since it's not already there
#loop through the words word list
#loop through indexes for the length of the word, which is the same for every word
#create the pattern with (word[:j] + "*" + word[j + 1 :])
#add the pattern to the nei dictionary as the key with the word as the value
#initialize a visit set with the begin word
#initialize a queue with the begin word
#initialize a result variable with 1
#while the queue is not empty
#loop through the queue, so we go through the full layer of neighbors
#pop the word from the queue
#check if the word is the end word
# if so, return the result

#loop through the indexes of the word
#initialize the pattern with (word[:j] + "*" + word[j + 1 :])
#loop through the neighbors of the pattern
#check if the neighbor is not in the visit set
# if so, add the neighbor to the visit set
#add the neighbor to the queue
#increment the result by 1 outside the for loop

#return 0 if it's never found

#bfs
#key in adjacency list is the pattern, value is the word
#pattern: word[:j] + "*" + word[j + 1 :]
#base case word == endWord

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0