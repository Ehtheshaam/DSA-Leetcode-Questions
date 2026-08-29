
class Solution:

    def permuteUnique(self, nums):
        result = []
        path = []
        used = [False] * len(nums)

        nums.sort()

        self.backtrack(nums, result, path, used)

        return result

    def backtrack(self, nums, result, path, used):

        # Complete permutation
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):

            # Already used
            if used[i]:
                continue

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # Choose
            used[i] = True
            path.append(nums[i])

            # Explore
            self.backtrack(nums, result, path, used)

            # Undo
            path.pop()
            used[i] = False

