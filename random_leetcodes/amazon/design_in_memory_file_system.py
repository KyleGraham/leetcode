# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

# Example 1:


# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]

# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/");                         // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/");                         // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"


#more of a LLC problem, this uses trienode aka prefix tree. Instead of prefixes it's directories tho
##time complexity: O(m*n) m is the length of the input string and n is the depth of the trie
#space complexity: O(m*n)

#trienode class
#initializes to self.content = "" and self.isfile = False, self.children = defaultdict(TrieNode)

#init filesystem
#initializes self.top as TrieNode

#ls
#splits the path by / and sets node to self.top
#loops through the path list and sets node to the children of the node
#checks if the node is a file, if so returns the name of the file
#otherwise, returns the sorted list of the children of the node

#mkdir
#splits the path by / and sets node to self.top
#loops through the path list
#sets the node to the children of the node at [p] in the path

#addContentToFile
#splits the path by / and sets node to self.top
#loops through the path list and sets node to the children of the node
#adds the content to the node and sets isfile to true

#readContentFromFile
#splits the path by / and sets node to self.top
#loops through the path list and sets node to the children of the node
#returns the content of the node




class TrieNode:
    def __init__(self):
        #prefix tree
        self.content = ""
        self.children = defaultdict(TrieNode)
        self.isfile = False

class FileSystem:

    def __init__(self):
        self.top = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_list = path.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        path_list = path.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children[p]
        
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_list = filePath.split("/")
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True
    

    def readContentFromFile(self, filePath: str) -> str:
        path_list = filePath.split('/')
        node = self.top
        for p in path_list:
            if not p:
                continue
            node = node.children.get(p)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
