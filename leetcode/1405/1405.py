import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for cnt, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))
        
        res = []
        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            cnt1 = -cnt1

            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                cnt2 = -cnt2

                res.append(ch2)
                cnt2 -= 1

                if cnt2 > 0:
                    heapq.heappush(heap, (-cnt2, ch2))
                heapq.heappush(heap, (-cnt1, ch1))
            else:
                res.append(ch1)
                cnt1 -= 1
                if cnt1 > 0:
                    heapq.heappush(heap, (-cnt1, ch1))
        return "".join(res)