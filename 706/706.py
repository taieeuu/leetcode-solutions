

class MyHashMap:

    def __init__(self):
        self.size = 10**6+1
        self.bucket = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        for i, kv in enumerate(self.bucket[idx]):
            if key == kv[0]:
                self.bucket[idx][i] = (key, value)
                found = True
                break
        if not found:
            self.bucket[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.size
        for (k, v) in self.bucket[idx]:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        for i, kv in enumerate(self.bucket[idx]):
            if kv[0] == key:
                del self.bucket[idx][i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)