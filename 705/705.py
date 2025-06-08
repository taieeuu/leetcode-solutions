class MyHashSet:

    def __init__(self):
        self.size = 10**6+1
        self.bucket = [[] for _ in range(self.size)]

    def _hash(self, n):
        return n % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.bucket[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if self.contains(key):
            self.bucket[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return True if key in self.bucket[idx] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)