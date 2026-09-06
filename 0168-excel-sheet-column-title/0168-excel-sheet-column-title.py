class Solution(object):
    def convertToTitle(self, columnNumber):

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = letters[columnNumber % 26] + result
            columnNumber = columnNumber // 26

        return result
        