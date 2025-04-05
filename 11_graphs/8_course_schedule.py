# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[0,1]]
# Output: true
# Explanation: First take course 1 (no prerequisites) and then take course 0.

# Example 2:
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false
# Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.


#dfs solution using adjacency list
# time complexity: O(V + E) where V is number of vertices and E is number of edges
# space complexity: O(V + E) where V is number of vertices and E is number of edges

#adjacency list is another way to display a graph basically, using a dictionary/hashmap
#key is the node, and the value is a list of the neighbors

#start by converting the array of arrays into a adjacency list
#initialize preMap as a dictionary with the course as the key and the prerequisites as the value
#preMap = {i:[] for i in range(numCourses)} if numCourses is 2, then it initializes as
# {0: [], 1: []}

#loop through the prerequisites and add the course as a key and the prerequisite as a value
#initialize a visitSet as set()

#loop through courses in range(numCourses), we have to do a loop because the courses may not be fully connected
#check if dfs returns false
# if so, return false
#otherwise, return true outside the loop

#dfs function, takes in crs
#check if the course is in the visit set
# if so, return false
#check if the course has no prerequisites
# if so, return true
#add the course to the visit set
#loop through the prerequisites of the course
#check if dfs returns false
# if so, return false
#remove the course from the visit set as we're no longer currently there
#remove the prerequisites of the course since we've already visited them and they returned true that we can complete them
#return true

#the visitSet checks for cycles, since if a course prereq is something we're already visinting, then we have a cycle



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #visitSet = all courses along the current dfs path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        #have to loop through all courses in case courses are not fully connected
        #1 -> 2
        #3 -> 4
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True