# collections 모듈에서 defaultdict를 불러옴 (기본값을 리스트로 설정하기 위함)
from collections import defaultdict

# 항공권 정보를 바탕으로 경로를 구하는 함수
def solution(tickets):
    # 그래프 초기화: 출발지를 key로, 도착지를 value 리스트로 저장
    graph = defaultdict(list)

    # 항공권 정보를 바탕으로 그래프 구성
    for (start, end) in tickets:
        graph[start].append(end)

    # 도착 공항 리스트를 내림차순으로 정렬
    # 스택에서 pop()으로 사전순 앞선 경로부터 탐색하기 위해
    for airport in graph:
        graph[airport].sort(reverse=True)

    # 결과 경로를 저장할 리스트
    path = []
    # DFS를 위한 스택, 시작점은 항상 "ICN"
    stack = ["ICN"]

    # 스택이 빌 때까지 반복
    while stack:
        # 현재 위치 (경로의 마지막 지점)
        route = stack[-1]

        # 현재 위치에서 더 이상 갈 수 있는 공항이 없을 경우
        if not graph[route]:
            # 경로에 추가하고, 스택에서 제거
            path.append(stack.pop())
        else:
            # 다음 목적지를 스택에 추가
            nextRoute = graph[route].pop()
            stack.append(nextRoute)

    # 경로를 역순으로 반환 (후위 순회 결과)
    return path[::-1]

# 테스트 케이스 실행
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# 결과: ["ICN", "JFK", "HND", "IAD"]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# 결과: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]