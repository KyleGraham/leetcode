# Implement an algorithm to serialize and deserialize a binary tree.
# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be 
# stored or sent across a network to be reconstructed later in another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. 
# There is no additional restriction on how your serialization/deserialization algorithm should work.
# Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# # Input: root = []
# Output: []


# optimum solution using dfs for both serialization and deserialization

#time complexity O(n)
#space complexity O(n)

#serialize
#initialize a class variable s_format to store the serialized string
#dfs function taking in the root
#we'll be using # as a delimiter
#check if the root is empty
#add N to the s_format if so, this indicates the null value in a way that our deserialize can read since nulls important
#add the value of the node to the s_format
#recursively call the function on the left and right

#call the dfs function with the root
#return the s_format state variable


#deserialize
#split the data string by the delimiter
#initialize a class variable i to 0 to keep track of the index
# we'll use this class variable to loop through the array

#dfs function
#check if the current value is N
#increment the index
#return None

#create a node with the current value
#increment the index
#set the node.left to the result of the dfs function
#set the node.right to the result of the dfs function
#return the node

#call the dfs function and return the result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s_format = ""

        def dfs(root):
            if not root:
                self.s_format += "N#"
                return
            self.s_format += str(root.val) + "#" 
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.s_format
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.datalist = data.split('#')
        self.i = 0

        def dfs():
            if self.datalist[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(self.datalist[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
