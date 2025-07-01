import heapq

def solution(N: int, M: int, tree: list, S: int, E: int):
    INF = float('inf')
    # 인접 리스트 초기화 (1번부터 N번까지)
    graph = [[] for _ in range(N + 1)]
    for u, v, w in tree:
        graph[u].append((v, w))

    # 거리 테이블 초기화
    dist = [INF] * (N + 1)
    dist[S] = 0

    # 우선순위 큐 (거리, 노드)
    pq = [(0, S)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        # 이미 더 짧은 거리 기록이 있다면 스킵
        if current_dist > dist[u]:
            continue
        # 도착점이라면 바로 반환 (최단 거리 확정)
        if u == E:
            return current_dist
        # 인접 노드 완화(relaxation)
        for v, w in graph[u]:
            new_cost = current_dist + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    # 도달 불가 시 INF 반환 대신 -1 등 처리 가능
    return dist[E] if dist[E] != INF else -1

# 📌 테스트 예시
print(solution(
    5, 8,
[
    [1, 2, 2],
    [1, 3, 3],
    [1, 4, 1],
    [1, 5, 10],
    [2, 4, 2],
    [3, 4, 1],
    [3, 5, 1],
    [4, 5, 3]
],
    1, 5
))