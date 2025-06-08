from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        count = {0:1}
        for num in nums:
            curSum += num
            if (curSum - k) in count:
                ans += count.get(curSum - k, 0)
            count[curSum] = count.get(curSum, 0) + 1
        return ans