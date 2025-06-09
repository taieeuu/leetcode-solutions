
class Tries:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        root = Tries()
        for words in dictionary:
            node = root
            for char in words:
                if char not in node.children:
                    node.children[char] = Tries()
                node = node.children[char]
            node.is_word = True
        n = len(s)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]

            node = root

            j = i

            while j < n and s[j] in node.children:
                node = node.children[s[j]]
                j += 1
                if node.is_word:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]

