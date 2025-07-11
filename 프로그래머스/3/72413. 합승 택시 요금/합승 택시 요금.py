# 시스템의 최대 정수값과 우선순위 큐(힙) 라이브러리를 가져옴
import sys, heapq

# 전체 문제 해결을 위한 메인 함수
def solution(n, s, a, b, fares):
    # 경로 비용 계산 시 무한대를 나타낼 값 설정
    inf = sys.maxsize

    # 각 지점의 인접 정보를 저장할 인접 리스트를 생성함
    maps = [[] for _ in range(n+1)]
    # 주어진 도로 정보(fares)를 순회하며 인접 리스트를 구성함
    for v, u, c in fares:
        # 도로는 양방향이므로, 양쪽 지점에 대해 각각 [연결된 지점, 요금] 정보를 추가함
        maps[v].append((u, c))
        maps[u].append((v, c))

    # 특정 지점에서 다른 모든 지점까지의 최단 거리를 계산하는 다익스트라 함수
    def dijkstra(start):
        # 각 지점까지의 최단 거리를 저장할 리스트를 생성하고, 초기값을 무한대로 설정함
        distance = [inf] * (n+1)
        # 시작 지점의 거리는 0으로 초기화함
        distance[start] = 0
        # 탐색할 노드를 (요금, 지점 번호) 형태로 저장할 우선순위 큐를 생성하고 시작 지점 정보를 넣음
        queue = [(0, start)]

        # 큐에 탐색할 지점이 남아있는 동안 반복함
        while queue:
            # 현재까지 가장 요금이 적은 지점의 정보(요금, 지점 번호)를 큐에서 꺼냄
            currentDist, currentNode = heapq.heappop(queue)

            # 큐에서 꺼낸 요금이 이미 알려진 최단 거리보다 크다면, 더 효율적인 경로가 이미 처리된 것이므로 건너뜀
            if distance[currentNode] < currentDist:
                continue

            # 현재 지점과 인접한 모든 지점을 순회함
            for nextNode, nextDist in maps[currentNode]:
                # 현재 지점을 거쳐 인접 지점으로 가는 새로운 경로의 요금을 계산함
                cost = currentDist + nextDist
                # 새로운 경로의 요금이 기존 최단 거리보다 저렴한 경우
                if cost < distance[nextNode]:
                    # 최단 거리를 새로운 값으로 갱신함
                    distance[nextNode] = cost
                    # 갱신된 요금과 지점 정보를 큐에 추가하여 다음 탐색에 반영함
                    heapq.heappush(queue, (cost, nextNode))
        # 시작 지점으로부터 모든 지점까지의 최단 거리 리스트를 반환함
        return distance

    # 출발지 s에서 모든 지점까지의 최단 거리를 계산
    distFromS = dijkstra(s)
    # A의 목적지 a에서 모든 지점까지의 최단 거리를 계산
    distFromA = dijkstra(a)
    # B의 목적지 b에서 모든 지점까지의 최단 거리를 계산
    distFromB = dijkstra(b)

    # 최소 요금을 저장할 변수를 무한대로 초기화함
    minFare = inf
    # 1번부터 n번까지 모든 지점을 합승 지점 후보로 하여 순회함
    for i in range(1, n + 1):
        # s->i(합승) + i->a(개별) + i->b(개별)의 총 요금을 계산함
        # i->a 거리는 a->i 거리와 같으므로 미리 계산된 값을 사용
        fare = distFromS[i] + distFromA[i] + distFromB[i]
        # 계산된 총 요금과 현재까지의 최소 요금을 비교하여 더 작은 값으로 갱신함
        minFare = min(minFare, fare)

    # 최종적으로 계산된 최소 요금을 반환함
    return minFare

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) #82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) #14
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) #18