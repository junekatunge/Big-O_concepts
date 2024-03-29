# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.





class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        i = 0

        def swap(i,j):
            temp = nums[i]#placing the actual value in a temporary variable then moving the pointer i to j 
            nums[i] = nums[j]#then moving valuej to i
            nums[j] = temp#then asgning the value j to temp
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
            if nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
        