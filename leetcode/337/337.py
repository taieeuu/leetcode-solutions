# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
		# Tree + DP + DFS
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int):
            if not node:
                return (0, 0)
            L_rob, L_not = dfs(node.left)
            R_rob, R_not = dfs(node.right)

            rob_this = node.val + L_not + R_not
            not_rob_this = max(L_rob, L_not) + max(R_rob, R_not)

            return (rob_this, not_rob_this)

        rob_root, not_rob_root = dfs(root)
        return max(rob_root, not_rob_root)
