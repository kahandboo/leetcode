class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and stack[-1] == i:
                del stack[-1]
            else:
                stack.append(i)

        return ''.join(stack)