from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if target == "0000":
            return 0
        if "0000" in dead:
            return -1
        
        def neighbors(code):
            ...
            for i, ch in enumerate(code):
                x = int(ch)
                for d in (-1, 1):
                    y = (x+d) % 10 
                    yield code[:i] + str(y) + code[i+1:]
        
        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            code, step = queue.popleft()

            for nxt in neighbors(code):
                if nxt in visited or nxt in dead:
                    continue
                if target == nxt:
                    return step + 1
                
                visited.add(nxt)
                queue.append((nxt, step+1))

        return -1