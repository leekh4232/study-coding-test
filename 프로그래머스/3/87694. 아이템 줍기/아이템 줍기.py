from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배 확장
    char_x, char_y = characterX * 2, characterY * 2
    item_x, item_y = itemX * 2, itemY * 2
    
    # 맵 생성 및 초기화 (최대 좌표 50 * 2 + 1)
    board = [[0] * 102 for _ in range(102)]
    
    # 직사각형 테두리 그리기
    for x1, y1, x2, y2 in rectangle:
        # 각 직사각형의 내부를 2로, 테두리를 1로 채움
        # 겹치는 부분은 내부가 우선하도록
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:
                    board[i][j] = 2
                elif board[i][j] != 2:
                    board[i][j] = 1
    
    # BFS를 위한 큐 생성, 시작점과 거리 0을 큐에 넣음
    q = deque([(char_x, char_y, 0)])
    # 방문 처리를 위해 시작점을 -1로 변경
    board[char_x][char_y] = -1
    
    # 상, 하, 좌, 우 이동 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y, dist = q.popleft()
        
        # 아이템 위치에 도착하면
        if x == item_x and y == item_y:
            # 최종 거리를 2로 나누어 반환 (좌표 확장했으므로)
            return dist // 2
        
        # 4가지 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 이동할 다음 위치가 맵의 범위 내에 있고
            if 0 <= nx <= 101 and 0 <= ny <= 101:
                # 다음 위치가 테두리이고 (값이 1), 아직 방문하지 않았으면
                if board[nx][ny] == 1:
                    # 방문 처리
                    board[nx][ny] = -1
                    # 다음 위치와 거리를 큐에 추가
                    q.append((nx, ny, dist + 1))
    
    return 0