class Solution(object):
    def findDisappearedNumbers(self, nums):
       
        n = len(nums)
        abuu = set()

        for i in range(n):
            abuu.add(nums[i])
        result = []
        for i in range(1,n+1):    
            if i not in abuu:
                result.append(i)
        return result        
        