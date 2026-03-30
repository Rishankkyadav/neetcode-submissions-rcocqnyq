class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictr = {}
        for i  , num in enumerate(nums):
            if target - num in dictr:
                return[dictr[target - num] , i]
            dictr[num] = i 

        