class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        slow = 0
        fast = 0
        s = ''.join(char.lower() for char in s if char.isalnum())
        while fast < len(s):
            stack.append(s[slow])
            slow += 1
            fast += 2
        
        if len(s)%2 == 1:
            stack.pop()
        
        while slow < len(s):
            if stack.pop() != s[slow]:
                return False
            slow += 1

            
        

        return True