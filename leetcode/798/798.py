from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        n = len(nums)
    
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k
        used = [False] * n

        def dfs(index: int) -> bool:
            if index == n:
                return True

            num = nums[index]
            
            for i in range(k):
                
                if buckets[i] + num <= target:
                    buckets[i] += num
                    used[index] = True

                    if dfs(index + 1):
                        return True

                    buckets[i] -= num
                    used[index] = False

                if buckets[i] == 0:
                    break

            return False
        return dfs(0)

