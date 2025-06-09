from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_set = {}
        output = 0
        for num in nums:
            if num not in nums_set:
                nums_set[num] = 0
            nums_set[num] += 1
        for k, v in nums_set.items():
            if k+1 in nums_set:
                output = max(output, nums_set[k] + nums_set[k+1])
        return output
