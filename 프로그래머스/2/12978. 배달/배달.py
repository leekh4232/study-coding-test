# 우선순위 큐(최소 힙) 자료구조를 사용하기 위해 heapq 라이브러리를 가져옴
import heapq

# 전체 문제 해결을 위한 메인 함수
def solution(n, road, k):
    # 각 마을의 인접 정보를 저장할 자료구조를 생성함
    # adj[i]는 i번 마을과 연결된 {상대 마을: 거리} 형태의 딕셔너리임
    adj = [{} for _ in range(n + 1)]
    # 주어진 모든 도로 정보에 대해 반복함
    for a, b, cost in road:
        # a번 마을에서 b번 마을로 가는 경로를 처리함. 기존 경로가 없거나 새로운 경로가 더 짧으면 정보를 갱신함
        if b not in adj[a] or cost < adj[a][b]:
            adj[a][b] = cost
        # b번 마을에서 a번 마을로 가는 경로를 처리함. 도로는 양방향이므로 반대 방향도 동일하게 처리함
        if a not in adj[b] or cost < adj[b][a]:
            adj[b][a] = cost

    # 1번 마을로부터 각 마을까지의 최단 거리를 저장할 리스트를 생성하고, 초기값을 무한대(float('inf'))로 설정함
    dist = [float('inf')] * (n + 1)
    # 출발점인 1번 마을의 거리는 0으로 초기화함
    dist[1] = 0

    # 다익스트라 알고리즘에 사용할 우선순위 큐(힙)를 생성하고, 시작 노드 정보를 [거리, 노드] 형태로 추가함
    heap = [[0, 1]]

    # 힙에 탐색할 노드가 남아있는 동안 반복함
    while heap:
        # 현재까지 가장 거리가 짧은 노드의 정보(비용, 노드 번호)를 힙에서 꺼냄
        cost, node = heapq.heappop(heap)

        # 힙에서 꺼낸 경로의 비용(cost)이 이미 알려진 최단 거리보다 크다면, 더 효율적인 경로가 이미 처리된 것이므로 건너뜀
        if cost > dist[node]:
            continue

        # 현재 노드와 인접한 모든 노드와 그 거리를 순회함
        for neighbor, weight in adj[node].items():
            # 현재 노드를 거쳐 인접 노드로 가는 새로운 경로의 비용을 계산함
            newCost = cost + weight
            # 새로운 경로의 비용이 기존 최단 거리보다 짧은 경우
            if newCost < dist[neighbor]:
                # 최단 거리를 새로운 값으로 갱신함
                dist[neighbor] = newCost
                # 갱신된 거리와 노드 정보를 힙에 추가하여 다음 탐색에 반영함
                heapq.heappush(heap, [newCost, neighbor])

    # 계산된 최단 거리 목록(dist)에서 배달 가능 시간(k) 이하인 마을의 수를 세어 반환함
    return len([i for i in dist if i <= k])