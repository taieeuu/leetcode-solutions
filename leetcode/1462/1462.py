from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        can_reach = [set() for _ in range(numCourses)]

        def dfs(course):
            for neighbor in graph[course]:
                if neighbor not in can_reach[course]:
                    can_reach[course].add(neighbor)
                    dfs(neighbor)
                    can_reach[course] |= can_reach[neighbor]
        
        for i in range(numCourses):
            dfs(i)

        return [v in can_reach[u] for u, v in queries]