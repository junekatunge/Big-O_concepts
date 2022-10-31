# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # create pointer
        l,r = 0, len(nums) - 1
        
        while l <= r:
            m = (l+r) // 2
            #if the index of the midpoint(m) is greater than target
            if nums[m] > target:
                r = m - 1
#                 if the index of the midpoint(m) is less than target
            if nums[m] < target:
                l = m + 1
            else:
                return m 
        return -1
            