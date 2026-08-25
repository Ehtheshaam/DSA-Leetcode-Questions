class Solution(object):
    def longestPalindrome(self, s):
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                x = s[i:j+1]

                if x == x[::-1] and len(x) > len(ans):
                    ans = x

        return ans