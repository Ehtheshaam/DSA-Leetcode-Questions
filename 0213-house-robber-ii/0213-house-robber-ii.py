class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        case1 = self.helper(nums[:-1])  # don't take last
        case2 = self.helper(nums[1:])   # don't take first

        return max(case1, case2)

    def helper(self, nums):
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]

        if n > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]