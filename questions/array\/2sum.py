class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # i is index n is the number
        for i,n in enumerate (nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i
        
        