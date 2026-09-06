class Solution(object):
    def isHappy(self, n):

        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            total = 0

            while n > 0:
                x = n % 10
                total += x ** 2
                n = n // 10

            n = total

        return True
        