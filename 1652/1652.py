from typing import List


class Solution:
		# sliding window
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []
        if k == 0:
            return [0] * n
        elif k < 0:
            p = -k
            window = sum(code[i] for i in range(n-p, n))
            res.append(window)
            for i in range(1, n):
                window += -code[(i-1-p)%n] + code[(i-1)%n]
                res.append(window)
                
        elif k > 0:
            window = sum(code[i] for i in range(1, k+1))
            res.append(window)
            for i in range(1, n):
                window += -code[i] + code[(i+k)%n]
                res.append(window)
        return res