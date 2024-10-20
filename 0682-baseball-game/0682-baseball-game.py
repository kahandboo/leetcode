class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            try:
                stack.append(int(i))
            except ValueError:
                if i == '+':
                    if len(stack) > 1:
                        new_score = stack[-1] + stack[-2]
                        stack.append(new_score)
                elif i == 'D':
                    if stack:
                        new_score = 2 * stack[-1]
                        stack.append(new_score)
                else:
                    if stack:
                        stack.pop()

        return sum(stack)
