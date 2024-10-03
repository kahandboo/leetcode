class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'(':')','{':'}','[':']'}
        for i in s:
            if i in bracket:
                stack.append(i)
            elif i in bracket.values():
                if not stack or bracket[stack.pop()] != i:
                    return False

        return not stack
            
