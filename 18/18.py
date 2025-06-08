from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        if length < 4:
            return []
        res = []
        for i in range(length-3):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, length-2):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                left, right = j+1, length-1
                while left < right:
                    cur_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if cur_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left+=1
                        right-=1
                    elif cur_sum < target:
                        left += 1
                    elif cur_sum > target:
                        right -= 1

        return res