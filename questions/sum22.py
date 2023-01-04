class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # i is index n is the number
        for i,n in enumerate (nums):
            diff = target - n
            if diff in hashmap:
                #return a pair of indices
                return [hashmap[diff],i]
                #otherwise assign it the index
            hashmap[n] = i
        
        