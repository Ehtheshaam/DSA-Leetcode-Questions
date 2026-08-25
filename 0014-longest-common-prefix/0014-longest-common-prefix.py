class Solution(object):
    def longestCommonPrefix(self, strs):
        res = strs[0]

        for s in strs:
            while not s.startswith(res):
                res = res[:-1]

        return res


        # res = ""
        # for i in range(len(strs[0])):
        #     ch = strs[0][i]
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != ch:
        #             return res
        #     res += ch
        # return res