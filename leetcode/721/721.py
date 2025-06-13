from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            for i in range(len(emails)):
                email_to_name[emails[i]] = name

            for i in range(0, len(emails)):
                email_graph[emails[0]].add(emails[i])
                email_graph[emails[i]].add(emails[0])
        
        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        visited = set()
        res = []
        for email in email_graph:
            if email not in visited:
                component = []
                dfs(email, component)
                res.append([email_to_name[email]] + sorted(component))

        return res

sol = Solution()

input_array = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]
result = sol.accountsMerge(input_array)
print(result)
