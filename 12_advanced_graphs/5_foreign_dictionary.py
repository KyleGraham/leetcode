# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, 
# where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. 
# If the order is invalid, return an empty string. 
# If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

# The first letter where they differ is smaller in a than in b.
# There is no index i such that a[i] != b[i] and a.length < b.length.
# Example 1:
# Input: ["z","o"]
# Output: "zo"
# Explanation:
# From "z" and "o", we know 'z' < 'o', so return "zo".

# Example 2:
# Input: ["hrn","hrf","er","enn","rfnn"]
# Output: "hernf"
# Explanation:
# from "hrn" and "hrf", we know 'n' < 'f'
# from "hrf" and "er", we know 'h' < 'e'
# from "er" and "enn", we know get 'r' < 'n'
# from "enn" and "rfnn" we know 'e'<'r'
# so one possibile solution is "hernf"



#solution using adj list and dfs doing topological sort
#time complexity: O(N + V + E) where V is number of vertices and E is number of edges and N is the sum of the lengths of all the strings
#space complexity: O(V + E) where V is number of vertices and E is number of edges 

#basically, we create an adjacency list for the characters in the words
#this is based on the initial ordering of the words
#we compare the words 2 by 2, checking the first character that differs in them
#then we create an edge from the first character to the second character, since that determines the order
# so with "hrn" and "hrf" the first differing character is "n" and "f", n comes before f so the graph would be n -> f

#we do a postorder traversal just incase the first node points to the second node and the first node also points to a third node. 
#with postorder, the order wouldn't be messed up because of this

#create an adj list with the characters as keys and a set as the value to take care of duplicates
#loop through 0 to len(words) - 1
#get the 2 words at i and i + 1, this is why we add the -1 to the range
#initialize minLen as the min length of the two words
#check if the first word is longer than the second word and the first minLen characters are the same, so they have the same prefix basically
# if so, return an empty string since we can't determine the order its invalid
#loop through the minLen characters
#check if the characters are not the same
# if so, add the first character to the adjacency list with the second character as the value
#break out of the loop since we found the first differing character
#initialize a visit dictionary, false = visited, true = visited and its in the path
#initialize a result list to store the characters in reverse order
#for the keys in the adj list:
#call dfs on the character
#check if dfs returns true
# if so, return an empty string since we have a cycle
#reverse the result list since we did a postorder traversal
#return the result list as a string

#the dfs function
#check if the character is in the visit dictionary
# if so, return the value of the visit dictionary, true or false

#add the character to the visit dictionary with true as the value
#loop through the neighbors of the character
#call dfs on the neighbor and check if it returns true, returning true if it does

#change the value of the character in the visit dictionary to false
#append the character to the result list


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            #if prefix is the same but len(w2) is greater than len(w1)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                #get first differing character in each word
                if w1[j] != w2[j]:
                    #add to adj list, with the first word being key
                    #second word being val
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} #false=visited, true=visited & path
        res = [] #will be in reverse order due to postorder dfs traversal

        def dfs(c):
            if c in visit:
                #detected loop
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            