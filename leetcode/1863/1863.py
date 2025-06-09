class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(i: int, x: int) -> int:
            # 處理完所有元素，回傳當前子集的 XOR 合計
            if i == len(nums):
                return x
            # 不選 nums[i]
            res = dfs(i+1, x)
            # 選 nums[i]
            res += dfs(i+1, x ^ nums[i])
            return res

        return dfs(0, 0)