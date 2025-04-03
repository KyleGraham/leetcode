# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

# Implement the PrefixTree class:

# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# Example 1:

# Input: 
# ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

# Output:
# [null, null, true, false, true, null, true]

# Explanation:
# PrefixTree prefixTree = new PrefixTree();
# prefixTree.insert("dog");
# prefixTree.search("dog");    // return true
# prefixTree.search("do");     // return false
# prefixTree.startsWith("do"); // return true
# prefixTree.insert("do");
# prefixTree.search("do");     // return true


#solution using a hash map
# #time complexity: O(n) for all functions
# #space complexity: O(t) for all functions where t is the total number of trienodes

#create a TrieNode class with children hashmap {} and endOfWord bool atribute defaulted to False

#create a PrefixTree class with a root TrieNode
#initialize the root TrieNode
#insert function that takes in a word
#set cur to root
#loop through the word
#check if the character is in the cur children
# if it is not, create a new TrieNode and set it to the cur children
# set cur to the cur children
# set cur endOfWord to True

#search function that takes in a word
# set cur to root
# loop through the word
# check if the character is in the cur children
# if it is not, return False
# set cur to the cur children
# return cur endOfWord. if it is not end of word it could be part of another word

#startsWith function that takes in a prefix
# set cur to root
# loop through the prefix
# check if the character is in the cur children
# if it is not, return False
# set cur to the cur children
# return True. Since it's a startswith we don't need to check if its the end of the word


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        return True