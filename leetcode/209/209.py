class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_length = 0
        output = float('inf')
        start = 0
        curr_sum = 0
        for end in range(len(nums)):
            curr_sum += nums[end]
            curr_length += 1
            while target <= curr_sum:
                output = min(output, curr_length)
                curr_sum -= nums[start]
                start += 1
                curr_length -= 1
        return output if output != float('inf') else 0
        