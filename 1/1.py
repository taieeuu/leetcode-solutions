class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        for indx, v in enumerate(nums):
            complement = target - v
            if complement in numsMap:
                return [numsMap[complement], indx]
            numsMap[v] = indx
        return []


sol = Solution()
nums = [2,7,11,15]
target = 9
res = sol.twoSum(nums, target)
print(res)