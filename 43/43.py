class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def convert_integer(num):
            res = 0
            for i in range(len(num)):
                res = res * 10 + (ord(num[i])-ord('0'))
            return res
        
        return str(convert_integer(num1) * convert_integer(num2))