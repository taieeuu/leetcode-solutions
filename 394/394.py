class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp_num = 0
        factor_num = ''
        for num in s:
            if num.isdigit():
                tmp_num = tmp_num * 10 + int(num)
            elif num == '[':
                stack.append(tmp_num)
                stack.append(num)
                tmp_num = 0
            elif num == ']':
                while stack and stack[-1]!='[':
                    factor_num = stack.pop() + factor_num
                stack.pop()
                repeat_time = stack.pop()
                stack.append(factor_num * int(repeat_time))
                factor_num = ''
            else:
                stack.append(num)
        return "".join(stack)


    

sol = Solution()
s = '3[a2[ac]]'
print(sol.decodeString(s))