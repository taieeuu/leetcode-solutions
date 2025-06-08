from collection import defaultdict
class DetectSquares:

    def __init__(self):
        self.d = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.d.keys():
            if (abs(x - px) != abs(y-py)) or px==x or py==y:
                continue
            res += self.d[(x, y)] * self.d.get((x, py), 0) * self.d.get((px, y), 0)
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)