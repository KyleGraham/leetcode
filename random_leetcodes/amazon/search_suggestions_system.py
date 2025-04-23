




class TrieNode:
    def __init__(self):
        #prefix tree
        self.children = {}
        self.suggestions = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        #insert each product into the Trie and store top 3 suggestions
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        #search each character of searchWord in the trie
        result = []
        node = root
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])
        return result