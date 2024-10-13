class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}

        for key in s:
            if key in my_dict.keys():
                my_dict[key] += 1
            else:
                my_dict[key] = 1

        for idx , key in enumerate(s):
            if my_dict[key] == 1:
                return idx
        
        return -1





        