"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ...
        
        def build(x, y, size):
            same = True
            first = grid[x][y]
            for i in range(x, x+size):
                for j in range(y, y+size):
                    if first != grid[i][j]:
                        same = False
                        break
                if not same:
                    break
            if same:
                return Node(
                    val=bool(first),
                    isLeaf=True
                )
            size = size // 2
            return Node(
                val=False,
                isLeaf=False,
                topLeft=build(x, y, size),
                topRight=build(x, y+size, size),
                bottomLeft=build(x+size, y, size),
                bottomRight=build(x+size, y+size, size)
            )

        grid_len = len(grid)
        root = build(0, 0, grid_len)
        return root