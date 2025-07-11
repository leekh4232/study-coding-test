def solution(arrows):
    # 8방향 이동을 위한 dx, dy 설정 (0~7 방향)
    dx = [0, 1, 1, 1, 0, -1, -1, -1]   # x축 이동값
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]   # y축 이동값

    # 시작 위치를 (0, 0)으로 설정
    x, y = 0, 0

    # 방문한 좌표(노드)를 저장할 Set
    visitedNode = set()
    visitedNode.add((x, y))   # 시작 노드 추가

    # 이동한 경로(간선)를 저장할 Set
    route = set()

    # 방(사이클) 개수
    cycle = 0

    # 주어진 방향 배열을 따라 이동
    for arrow in arrows:
        # 대각선 교차점을 정확히 처리하기 위해 한 방향 이동을 두 번 수행
        for _ in range(2):
            # 다음 좌표 계산
            nx, ny = x + dx[arrow], y + dy[arrow]

            # 이미 방문한 노드인데, 처음 가는 경로라면 방이 생김
            if (nx, ny) in visitedNode and (x, y, nx, ny) not in route:
                cycle += 1

            # 이동 경로(간선)를 양방향으로 기록
            route.add((x, y, nx, ny))
            route.add((nx, ny, x, y))

            # 방문한 좌표(노드)를 기록
            visitedNode.add((nx, ny))

            # 현재 위치 갱신
            x, y = nx, ny

    return cycle

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
