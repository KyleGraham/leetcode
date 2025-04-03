# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
# word may contain dots '.' where dots can be matched with any letter.

# Example 1:
# Input:
# ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
# Output:
# [null, null, null, null, false, true, true, true]
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("day");
# wordDictionary.addWord("bay");
# wordDictionary.addWord("may");
# wordDictionary.search("say"); // return false
# wordDictionary.search("day"); // return true
# wordDictionary.search(".ay"); // return true
# wordDictionary.search("b.."); // return true


# solution that uses a Trie and depth first search to find the word
# time complexity O(n) for all functions
# space complexity O(t + n) where n is the len of string and t is the total number of trienodes
# create a TrieNode class with children hashmap {} and endOfWord bool atribute defaulted to False
# create a WordDictionary class with a root TrieNode
# initialize the root TrieNode
# addWord function that takes in a word
#same as prev implement prefix tree problem
# set cur to root
# loop through the word
# check if the character is in the cur children
# if it is not, create a new TrieNode and set it to the cur children
# set cur to the cur children
# set cur endOfWord to True

# search function that takes in a word
# define a dfs function that takes in j and root. J is the current index of the search
# set cur to root
# loop through the word starting at j to end of word
# check if the character is a dot
# if it is, loop through the cur children and call dfs on each child with i+1 as j and the child TrieNode as the root
#dfs is called as an if statement. If it returns true, return True
# if it doesn't return from here, return False

#else statement from checking for . character
#just standard search here
#check if the character is in the cur children
# if it is not, return False
# set cur to the cur children
#return cur.endOfWord at the end of the loop
#then return the initial dfs call with 0 and root


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        #must check all words in children if '.' appears
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)