class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()  # 用來記錄已訪問的點
        min_heap = [(0, 0)]  # (距離, 點的索引)
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            # 標記當前點為已訪問
            visited.add(i)
            total_cost += cost

            # 更新與當前點相鄰的邊
            for j in range(n):
                if j not in visited:
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (distance, j))

        return total_cost
    
#==============================================
# k's algorithm
#==============================================

class UFS:
    def __init__(self, length):
        self.parent = list(range(length))
        self.rank = [0] * length
    
    def find(self, x):
        # find parent/group
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # union two groups
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False

        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        
        return True
    
class Solution:
    def minCostConnectPoints(self, points):
        length = len(points)

        ufs = UFS(length)

        if length == 0:
            return 0

        ary = []
        
        for i, (x1, y1) in enumerate(points):
            for j, in range(i+1, length):
                x2, y2 = points[j]
                dis = abs(x1 - x2) + abs(y1 - y2)
                ary.append((dis, i, j))

        ary.sort()

        res = 0
        for dis, i, j in ary:
            if ufs.union(i, j):
                res += dis

        return res
