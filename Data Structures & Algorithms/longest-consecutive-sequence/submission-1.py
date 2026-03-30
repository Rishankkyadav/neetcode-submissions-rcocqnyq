class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        max_len = 1
        nums = sorted(set(nums))
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
                max_len = max(count , max_len)
            else:
                count = 1
        return max_len


