import heapq

def solution(N: int, M: int, tree: list, S: int, E: int) -> int:
    INF = float('inf')
    # 1. 인접 리스트 초기화
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in tree:
        graph[u].append((v, w))

    # 2. 거리 테이블 딕셔너리 형태
    dist = {node: INF for node in graph}
    dist[S] = 0

    # 3. 우선순위 큐 초기화 (거리, 노드)
    pq = [(0, S)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        # 4. 이미 더 짧은 경로가 등록되어 있다면 무시
        if current_dist > dist[u]:
            continue
        # 5. 인접 노드 완화
        for v, w in graph[u]:
            new_cost = current_dist + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return int(dist[E])


# 📌 테스트 예시
print(solution(5, 8,
    [ [1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10],
      [2, 4, 2], [3, 4, 1], [3, 5, 1], [4, 5, 3] ],
    1, 5))