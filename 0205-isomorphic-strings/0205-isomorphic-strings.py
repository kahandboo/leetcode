class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        hashtable = {}
        while i < len(s):
            if s[i] in hashtable.keys():
                if hashtable[s[i]] != t[i]:
                    return False
            elif t[i] in hashtable.values():
                if s[i] != [k for k, v in hashtable.items() if v == t[i]]:
                    return False
            else:
                hashtable[s[i]] = t[i]
            i += 1
        return True