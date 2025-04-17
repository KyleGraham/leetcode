# You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

# Add - new points can be added to the stream into a data structure. 
# Duplicate points are allowed and should be treated as separate points.
# Query - Given a single query point, count the number of ways to choose three 
# additional points from the data structure such that the three points and the query point form a square.
# The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed.
# Recall that a square must have four equal sides.

# Implement the CountSquares class:

# CountSquares() Initializes the object.
# void add(int[] point) Adds a new point point = [x, y].
# int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.

# Example 1:
# # Input: 
# ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]
       
# Output:
# [null, null, null, null, 1, 0, null, 2]

# Explanation:
# CountSquares countSquares = new CountSquares();
# countSquares.add([1, 1]);
# countSquares.add([2, 2]);
# countSquares.add([1, 2]);

# countSquares.count([2, 1]);   // return 1.
# countSquares.count([3, 3]);   // return 0.
# countSquares.add([2, 2]);     // Duplicate points are allowed.
# countSquares.count([2, 1]);   // return 2. 

#solution using iteration
#time complexity: O(1) for add, O(n) for count
#space complexity: O(n) where n is the number of points


#basically uses geometry to check if the points are in a square
#given the point px, py, we can check if the given point is the opposite corner x, y
#then the top left corner will be (x, py) and the bottom right corner will be (px, y)

#init
#initialize ptsCount as a defaultdict of int, this will initialize the value to 0 if the key doesn't exist
#initialize pts as an empty array

#add function
#takes in a point
#increment the ptsCount by 1 for the given point, havae to convert point to tuple since list doesn't work as dict key
#append the point to the pts array

#count function
#takes in a point
#initialize res as 0
#initialize px, py as the point
#loop through the pts array
#check the geometry of the square and make sure points aren't stacked up
#check (abs(py - y) != abs(px - x)) or x == px or y == py
#continue if so

#increment res by the ptsCount of the top left corner (x, py) and the bottom right corner (px, y)
#return res


class CountSquares:
  
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1 #list cant be key, convert to tuple
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            #check the geometry of the square
            #also make sure points aren't stacked up ontop of eachother
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            #if one is 0, will be 0. 1s will be 1s, duplicates will increase
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res