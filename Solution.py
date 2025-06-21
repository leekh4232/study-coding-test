import heapq

data = [5, 1, 3, 2, 8, 7]
max_heap = []
for x in data:
    heapq.heappush(max_heap, -x)  # 삽입 시 부호 반전

print("Max 힙 루트 (가장 큰 원소):", -max_heap[0])

while max_heap:
    print(-heapq.heappop(max_heap))  # 꺼낼 때도 부호 다시 반전