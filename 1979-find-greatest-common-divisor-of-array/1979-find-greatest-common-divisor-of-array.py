class Solution(object):
    def findGCD(self, nums):
        
        small = min(nums)
        largest = max(nums)

        while small!=0:
            largest,small = small,largest%small
        return largest    