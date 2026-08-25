class Solution(object):
    def strStr(self, haystack, needle):
        # for i in range(len(haystack)):
        #     if haystack.startswith(needle, i):
        #         return i
        # return -1

        return haystack.find(needle)