class Solution(object):
    def maximumGap(self, nums):
        max_gap = 0
        nums.sort()
        for i in range(len(nums)):
            max_gap = max(max_gap,nums[i]-nums[i-1])
        return max_gap    