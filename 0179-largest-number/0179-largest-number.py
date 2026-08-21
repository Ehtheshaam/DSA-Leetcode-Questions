class Solution(object):
    def largestNumber(self, nums):

        # Convert numbers to strings
        s = []

        for i in range(len(nums)):
            s.append(str(nums[i]))

        # Compare two numbers at a time
        for i in range(len(s)):
            for j in range(len(s) - 1):

                if s[j] + s[j + 1] < s[j + 1] + s[j]:
                    s[j], s[j + 1] = s[j + 1], s[j]

        # Join all strings
        result = ""

        for num in s:
            result += num

        # Handle case like [0, 0]
        if result[0] == "0":
            return "0"

        return result