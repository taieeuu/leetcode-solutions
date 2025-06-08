class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(cap):
            d = 1
            total = 0
            for weight in weights:
                if total+weight > cap:
                    d+=1
                    total = 0
                total += weight
            return d <= days
        
        left = max(weights)
        right = sum(weights)

        while left<=right:
            mid_cap = (left+right) // 2
            if can_ship(mid_cap):
                right = mid_cap - 1
            else:
                left = mid_cap + 1
        return left
