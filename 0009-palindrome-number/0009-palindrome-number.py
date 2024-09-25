class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        origin = x
        while(x>0):
            reverse = reverse*10 + x%10
            x = x//10
        if origin == reverse:
            return True
        else:
            return False