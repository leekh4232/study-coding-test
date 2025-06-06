import heapq

def solution(A: list, K: int) -> int:
    heapq.heapify(A)            # 리스트 A를 Min-Heap으로 변환 : O(n)

    for _ in range(K - 1):      # 가장 작은 값을 K-1번 제거 : O(n-1)
        heapq.heappop(A)

    return heapq.heappop(A)     # K번째로 작은 값 반환 : O(1)

print(solution([4, 1, 2, 3, 5], 2))