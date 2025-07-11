def solution(n, results):
    # 선수 간 승패 관계를 저장할 인접 행렬 생성 (0: 미확정, 1: 승리, -1: 패배)
    graph = [[0] * n for _ in range(n)]

    # 주어진 경기 결과를 인접 행렬에 기록
    for A, B in results:
        graph[A - 1][B - 1] = 1     # A 선수가 B 선수를 이김
        graph[B - 1][A - 1] = -1    # B 선수는 A 선수에게 패배

    # 플로이드-워셜 알고리즘으로 간접적인 승패 관계를 유추
    for i in range(n):          # 중간 경유 선수 i
        for j in range(n):      # 시작 선수 j
            for k in range(n):  # 도착 선수 k
                # 이미 승패가 결정된 경우 건너뜀
                if graph[j][k] != 0:
                    continue
                # j가 i를 이기고, i가 k를 이기면, j가 k를 이김
                if graph[j][i] == 1 and graph[i][k] == 1:
                    graph[j][k] = 1
                # j가 i에게 지고, i가 k에게 지면, j도 k에게 짐
                elif graph[j][i] == -1 and graph[i][k] == -1:
                    graph[j][k] = -1

    answer = 0

    # 각 선수별로 승패가 확정된 상대 선수가 n-1명인지 확인
    for g in graph:
        # 승패가 확정된 상대 수 계산
        if len(list(filter(lambda x: x != 0, g))) == n - 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
