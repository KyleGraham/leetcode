# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

#dfs solution using adjacency list
# time complexity: O(V + E) where V is number of vertices and E is number of edges
# space complexity: O(V + E) where V is number of vertices and E is number of edges

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

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True