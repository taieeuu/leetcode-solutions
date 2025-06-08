from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m-1, n-1, m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p-=1
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p-=1
                p2-=1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]

        return nums1
            
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
            """  
        nums1[m:] = nums2[:]
        nums1.sort()
        return nums1
    