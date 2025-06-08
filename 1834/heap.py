class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            parent = self.parent(i)
            self.swap(i, parent)
            i = parent

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_value

    def print_heap(self):
        print("Heap elements:", self.heap)

# 使用範例
heap = MaxHeap()
heap.insert(35)
heap.insert(33)
heap.insert(42)
heap.insert(10)
heap.insert(14)
heap.insert(19)
heap.insert(27)
heap.insert(44)
heap.insert(26)
heap.insert(31)
heap.print_heap()
max_value = heap.extract_max()
print("Maximum element:", max_value)
