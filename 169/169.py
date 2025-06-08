from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        idx, c = 0, 1
        for i in range(1, len(nums)):
            if nums[idx]==nums[i]:
                c += 1
            else:
                c -= 1
                if c < 0:
                    idx = i
                    c = 1
        return nums[idx]

