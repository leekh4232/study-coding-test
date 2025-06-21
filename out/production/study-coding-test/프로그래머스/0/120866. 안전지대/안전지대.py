def solution(board):
    # 8방향 탐색을 위한 방향배열 (위, 아래, 좌, 우, 대각선)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    # board의 크기
    n = len(board)

    # 지뢰가 있는 위치를 확인하여 위험지역 설정
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 경우
                for k in range(8):  # 8방향 탐색
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # 유효한 좌표인지 확인 후 위험지역(2)로 표시
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                        board[nr][nc] = 2  # 위험지역으로 설정

    # 안전한 지역(0의 개수) 카운트
    answer = sum(row.count(0) for row in board)

    return answer  # 안전한 지역의 개수 반환

# ✅ 예제 테스트 실행
board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]
print(solution(board))  # 결과: 16 (안전한 칸 수)

board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0]]
print(solution(board))  # 결과: 13 (안전한 칸 수)

board = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
print(solution(board))  # 결과: 0 (모든 칸이 위험지역)
