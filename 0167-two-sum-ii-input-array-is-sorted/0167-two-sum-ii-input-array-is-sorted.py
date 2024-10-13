class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in my_dict.keys():
                return list([my_dict[numbers[i]]+1,i+1])
            my_dict[target - numbers[i]] = i