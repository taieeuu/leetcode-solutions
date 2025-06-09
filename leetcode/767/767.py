import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0)+1

        n = len(s)
        max_s_len = max(s_freq.values())
        if max_s_len > (n+1)//2:
            return ""
        
        max_heap = [(-cnt, char) for char, cnt in s_freq.items()]
        heapq.heapify(max_heap)

        res = ""
        while len(max_heap) > 1:
            cnt1, ch1 = heapq.heappop(max_heap)
            cnt2, ch2 = heapq.heappop(max_heap)

            res+=ch1+ch2

            if cnt1+1 < 0:
                heapq.heappush(max_heap, (cnt1+1, ch1))
            if cnt2+1 < 0:
                heapq.heappush(max_heap, (cnt2+1, ch2))

        if max_heap:
            cnt, ch = heapq.heappop(max_heap)
            res += ch
        return res
        
