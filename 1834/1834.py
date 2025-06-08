import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks_with_idx = [
            (task[0], task[1], idx)
            for idx, task in enumerate(tasks)
        ]
        tasks_with_idx.sort(key = lambda x: x[0])
        result = []
        time = 0
        i = 0
        n = len(tasks_with_idx)
        min_heap = []
        heapq.heapify(min_heap)

        while min_heap or i<n:
            if not min_heap and time < tasks_with_idx[i][0]:
                time = tasks_with_idx[i][0]

            while i < n and tasks_with_idx[i][0]<=time:
                heapq.heappush(min_heap, (tasks_with_idx[i][1], tasks_with_idx[i][2]))
                i+=1
            
            prc, idx = heapq.heappop(min_heap)
            time+=prc
            result.append(idx)
        return result