class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)<=1:
            return 0
        
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
        if nums[0] > nums[1]:
            return 0    
        return len(nums) - 1