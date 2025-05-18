

#solution using sets
#time complexity O(n + m)
#space complexity O(n + m)

#use sets to get rid of duplicates and for faster checks if the number is present in the set
#make nums1 and nums2 a set
#initialize two arrays for results

#loop through set 1
#check if the num is in set 2, if not, add to the result1
#same thing for 2
#return the two arrays as one


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one = set(nums1)
        two = set(nums2)
        res1 = []
        res2 = []

        for num in one:
            if num not in two:
                res1.append(num)
        for num in two:
            if num not in one:
                res2.append(num)
        return [res1, res2]