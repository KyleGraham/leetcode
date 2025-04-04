#this one is a lot

# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. 
# Return the median value among all elements of the two arrays.
# Your solution must run in O(log(m+n)) time 

# Example 1:
# Input: nums1 = [1,2], nums2 = [3]
# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:
# Input: nums1 = [1,3], nums2 = [2,4]
# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

# basically, we're running binary search on the smaller array
# we want to find the left partitial of each array so that the partitians together make up a smaller sorted array to get the median of

# first we initialize A and B to the two arrays, then make sure A is always smaller than b
# then we get the total length of both arrays and half the total
#The half value will be used for the binary search of the bigger array

# we then set the left and right pointers for the binary search of the smaller array

#i is the regular mid point of the smaller array
# j is the mid point of the bigger array, but we have to subtract 2 because we have two arrays since its the total length in indexes

# we then calculate the left and right values of the partitions
# since these values can not exist and cause edge cases, they are defaulted to -infinity for left and infinity for right

# we know the partitians are correct if 
# Aleft <= Bright and Bleft <= Aright
# then we calculate the median 
# if odd, just gets the min
# if even, gets the average of the max of the left and the min of the right and divides by 2

# to increment the pointers:
# if Aleft > Bright, we move the right pointer to the left
# otherwise we move the left pointer to the right

#lets just hope I never see this in an interview

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        #Make sure A is always the smaller array
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #A
            j = half - i - 2 # have to remove 2 because two arrays, just double -1

            Aleft = A[i] if i >= 0 else float("-infinity") #edge case
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity") # edge case
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
