from typing import List

## merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        
        mid = len(nums)//2
        print(f"{nums[:mid]=}, {nums[mid:]=}")
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        print(f"{left=}, {right=}")
        return self.merge(left, right)
    
    def merge(self, left, right):
        q = p = 0
        merged = []
        while p < len(left) and q < len(right):
            if left[p] < right[q]:
                merged.append(left[p])
                p += 1
            else:
                merged.append(right[q])
                q += 1
        merged = merged + left[p:] + right[q:]
        print(f"{merged=}")
        return merged
    
if __name__ == '__main__':
    nums = [5,1,9,1,2,0,0]
    sol = Solution()
    res = sol.sortArray(nums)
    print(res)