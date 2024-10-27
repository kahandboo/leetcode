class Solution:
    def romanToInt(self, s: str) -> int:
        hashtable = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)-1):
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                result -= hashtable[s[i]]
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                result -= hashtable[s[i]]
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                result -= hashtable[s[i]]
            else:
                result += hashtable[s[i]]

        result += hashtable[s[-1]]

        return result