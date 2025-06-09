class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i]<0 or nums[i]>=len(nums):
                nums[i]=0

        for i in range(n):
            nums[nums[i]%n] += n

        for i in range(n):
            if nums[i] < n:
                return i
        return n
    
sol = Solution()
nums = [1,2,0]
res = sol.firstMissingPositive(nums)
print(nums)