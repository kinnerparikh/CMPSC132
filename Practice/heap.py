import heapq

a = [10, 12, 1, 14, 3, 17, 7, 2, 5, 8, 6, 70]
heapq._heapify_max(a)
heapq.heappop(a)
heapq._heapify_max(a)
heapq.heappop(a)
heapq._heapify_max(a)
heapq.heappop(a)
heapq._heapify_max(a)

print(a)