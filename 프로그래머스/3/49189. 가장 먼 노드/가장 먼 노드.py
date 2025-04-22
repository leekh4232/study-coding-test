from collections import deque

def solution(n, edge):
    answer = 0

    # 노드 간 연결 정보를 저장할 인접 리스트 생성 (노드 번호가 1부터 시작하므로 n+1 크기로 생성)
    graph = [[] for _ in range(n + 1)]

    # 각 노드까지의 최단거리를 저장할 리스트, 초기값은 모두 -1로 설정 (방문하지 않음을 의미)
    distance = [-1] * (n + 1)

    # 간선 정보를 바탕으로 양방향 그래프 구성
    for e in edge:
        graph[e[0]].append(e[1])  # 노드 e[0]에 e[1] 연결
        graph[e[1]].append(e[0])  # 노드 e[1]에 e[0] 연결

    # BFS를 위한 큐 초기화, 시작 노드는 1번
    queue = deque([1])

    # 시작 노드의 최단거리를 0으로 설정
    distance[1] = 0

    # BFS 수행 시작
    while queue:
        # 큐에서 현재 탐색할 노드를 꺼냄
        now = queue.popleft()

        # 현재 노드와 연결된 모든 노드 탐색
        for i in graph[now]:
            # 아직 방문하지 않은 노드라면
            if distance[i] == -1:
                queue.append(i)  # 큐에 추가하여 다음 탐색 대상으로 설정
                distance[i] = distance[now] + 1  # 현재 노드의 거리 +1로 최단거리 갱신

    # 최단거리 리스트에서 가장 큰 값을 찾아 해당 거리와 같은 노드의 개수를 계산
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))