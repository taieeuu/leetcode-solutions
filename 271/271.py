# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         res = ""
#         for c in strs:
#             res = res + '|' + c
#         return res
#     def decode(self, s: str) -> List[str]:
#         return s.split('|')[1:]

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for c in strs:
            res += str(len(c)) + '#' + c
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res