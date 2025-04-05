
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. 
# If there are many valid answers, return any of them. 
# If it's not possible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 3, prerequisites = [[1,0]]
# Output: [0,1,2]
# Explanation: We must ensure that course 0 is taken before course 1.

# Example 2:
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
# Output: []
# Explanation: It's impossible to finish all courses.

#basically just use a set to keep track of the visited courses that have been added to the output then do the same thing
#optimum solution using dfs and adjacency list for topological sort
# time complexity: O(V + E) where V is number of vertices and E is number of edges
# space complexity: O(V + E) where V is number of vertices and E is number of edges

# essentially, instead of visitSet checking for cycles, we use a cycle set
#we use a visit set for the courses that have been added to the output already

#rest is basically the same
#initialize preMap as a dictionary with the course as the key and the prerequisites as the value
#preMap = {i:[] for i in range(numCourses)} if numCourses is 2, then it initializes as
# {0: [], 1: []}
#initialize an output list
#initialize a visit set for nodes we've already added to the output
#initialize a cycle set for nodes we're currently visiting
#loop through the courses in range(numCourses)
#check if dfs returns false
# if so, return an empty list since cycle detected and its not possible
#otherwise, return the output outside the loop outside the loop

#the dfs function
#takes in crs
#check if the course is in the cycle set
# if so, return false since we have a cycle
#check if the course is in the visit set
# if so, return true since we've already added it to the output
#add the course to the cycle set
#loop through the prerequisites of the course
#check if dfs returns false
# if so, return false since we have a cycle
#remove the course from the cycle set since we're done visiting it
#add the course to the visit set 
#add the course to the output
#return true


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #a course has 3 possible states
        #visited -> crs has been added to output
        #visiting -> crs not added to output, but added to cycle
        #unvisited -> crs not added to output or cycle
        output = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
