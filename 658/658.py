class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        while len(arr) > k:
            if abs(arr[0] - x) <= abs(arr[-1] - x):
                arr.pop(-1)
            else:
                arr.pop(0)
        return arr