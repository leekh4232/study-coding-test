from collections import deque

def solution(maps):
    # 맵의 세로, 가로 길이
    n = len(maps)
    m = len(maps[0])
    
    # 상, 하, 좌, 우 이동 방향 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # BFS 탐색을 위한 큐 생성, 시작점 (0, 0)을 큐에 넣음
    queue = deque([(0, 0)])
    
    # BFS 시작
    while queue:
        # 큐에서 현재 위치를 꺼냄
        x, y = queue.popleft()
        
        # 현재 위치가 상대 팀 진영(도착점)이면
        if x == n - 1 and y == m - 1:
            # 도착점까지의 거리를 반환
            return maps[x][y]
        
        # 4가지 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동할 다음 위치가 맵의 범위 내에 있고
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 위치가 벽이 아니고 (값이 1이고), 아직 방문하지 않았으면
                if maps[nx][ny] == 1:
                    # 다음 위치까지의 거리를 현재 위치 거리 + 1로 업데이트
                    maps[nx][ny] = maps[x][y] + 1
                    # 다음 위치를 큐에 추가하여 탐색을 이어감
                    queue.append((nx, ny))
                    
    # 큐가 모두 비워질 때까지 도착점에 도달하지 못했으면
    return -1