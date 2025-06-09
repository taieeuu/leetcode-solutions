

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(start):
            if len(path)+(n-start+1)<k:
                return
            if len(path) == k:
                res.append(path.copy())
                return 
            for num in range(start, n+1):
                path.append(num)
                dfs(num+1)
                path.pop()

        dfs(1)
        return res

