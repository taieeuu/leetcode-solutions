# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:
#             if s[l] != s[r]:
#                 skipL = s[l+1 : r+1]
#                 skipR = s[l : r]
#                 return skipL == skipL[::-1] or skipR == skipR[::-1]
#             l += 1
#             r -= 1
#         return True
    
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -=1
            return True
        if not s:
            return True
        l, r = 0, len(s) -1
        while l< r:
            if s[l]!=s[r]:
                return is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1)
            l += 1
            r -= 1
        return True

