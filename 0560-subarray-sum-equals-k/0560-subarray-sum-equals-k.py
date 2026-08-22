class Solution(object):
    def subarraySum(self, nums, k):

        count = 0
        curr_sum = 0
        freq = {0: 1}

        for num in nums:
            curr_sum += num

            if curr_sum - k in freq:
                count += freq[curr_sum - k]

            if curr_sum in freq:
                freq[curr_sum] += 1
            else:
                freq[curr_sum] = 1

        return count