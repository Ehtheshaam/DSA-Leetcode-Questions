class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(i, current):
            result.append(current[:])

            for j in range(i, len(nums)):

                if j > i and nums[j] == nums[j - 1]:
                    continue

                current.append(nums[j])
                backtrack(j + 1, current)
                current.pop()

        backtrack(0, [])

        return result





