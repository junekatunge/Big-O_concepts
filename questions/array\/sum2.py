class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range ((i+1),len(nums)):
                sum = nums[i] + nums[j]#add the values at interger 
                if target == sum:
                    return [i,j]
        