class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        lower_s = lower_s.strip()
        reversed_lower_s = "".join(filter(str.isalnum, lower_s))
        if reversed_lower_s[::-1] == reversed_lower_s:
            return True
        return False
        
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
