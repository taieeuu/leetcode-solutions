from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (s, e), val in zip(equations, values):
            graph[s][e] = val
            graph[e][s] = 1 / val

        def dfs(s, e, visited):
            if e not in graph or s not in graph:
                return -1
            if s == e:
                return 1
            visited.add(s)
            for neighbor, val in graph[s].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, e, visited)
                if res!=-1:
                    return res * val
            return -1  

        results = []
        for s, e in queries:
            res = dfs(s, e, set())
            results.append(res)

        return results