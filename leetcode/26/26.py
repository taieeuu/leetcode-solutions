from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:] = unique + ['_'] * (len(nums)-len(unique))
        
        return len(unique)
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = None
        ptr = 0
        for num in nums:
            if num != prev:
                nums[ptr] = num
                ptr+=1
                prev = num
                
        return ptr