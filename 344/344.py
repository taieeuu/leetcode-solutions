from types import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r, l = len(s)-1, 0
        while l < r:
            s[r], s[l] = s[l], s[r]

            l+=1
            r-=1
        return s
