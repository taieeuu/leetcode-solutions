class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for (n, fr, to) in trips:
            events.append((fr, n))
            events.append((to, -n))

        events.sort(key=lambda x: (x[0], x[1]))

        cur = 0
        for fr, n in events:
            cur += n
            if cur > capacity:
                return False
        return True