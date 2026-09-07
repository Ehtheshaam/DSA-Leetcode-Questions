class Solution(object):
    def minRemoveToMakeValid(self, s):

        stack = []
        remove = set()

        # First pass
        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':

                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # Remaining '(' are invalid
        while stack:
            remove.add(stack.pop())

        # Build answer
        result = []

        for i in range(len(s)):
            if i not in remove:
                result.append(s[i])

        return ''.join(result)