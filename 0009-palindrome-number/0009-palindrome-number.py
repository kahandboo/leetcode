class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == '-':
            return False

        stack = []

        if len(x) % 2 == 0:
            for i in range(len(x)//2):
                stack.append(x[i])

            for j in range(len(x)//2, len(x)):
                val = stack.pop()
                if val != x[j]:
                    return False

            return True

        else:
            for i in range(len(x)//2):
                stack.append(x[i])

            for j in range(len(x)//2 + 1, len(x)):
                val = stack.pop()
                if val != x[j]:
                    return False

            return True
            
            
