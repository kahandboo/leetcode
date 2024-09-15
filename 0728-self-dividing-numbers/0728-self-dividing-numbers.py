class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left,right+1):
            temp = n
            is_dividing_number = True
            while temp > 0:
                digit = temp % 10
                if(digit == 0 or n%digit != 0):
                    is_dividing_number = False
                    break
                temp//=10 
            if is_dividing_number == True:
                result.append(n)
        
        return result
                
                        