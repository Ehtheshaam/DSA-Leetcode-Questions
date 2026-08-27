class Solution(object):
    def addDigits(self, num):
        s = str(num)

        while len(s) > 1:
            add = 0

            for ch in s:
                add = add + int(ch)

            s = str(add)

        return int(s)
        