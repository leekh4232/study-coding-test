from collections import deque

def normalize(block):
    # 블록의 좌표들을 (0, 0)을 기준으로 정규화
    min_x, min_y = min(x for x, y in block), min(y for x, y in block)
    return sorted([(x - min_x, y - min_y) for x, y in block])

def rotate(block):
    # 블록을 90도 회전
    max_x = max(x for x, y in block)
    return normalize([(y, max_x - x) for x, y in block])

def find_blocks(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    blocks = []
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                block = []
                q = deque([(i, j)])
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    block.append((x, y))
                    
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and \
                           board[nx][ny] == target and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                blocks.append(normalize(block))
                
    return blocks

def solution(game_board, table):
    answer = 0
    
    # game_board에서 빈칸 덩어리들을 찾음
    empty_blocks = find_blocks(game_board, 0)
    
    # table에서 퍼즐 조각 덩어리들을 찾음
    puzzle_blocks = find_blocks(table, 1)
    
    # 사용된 퍼즐 조각을 표시하는 리스트
    used_puzzles = [False] * len(puzzle_blocks)
    
    # 빈칸 덩어리를 하나씩 순회
    for empty in empty_blocks:
        for i in range(len(puzzle_blocks)):
            # 아직 사용되지 않은 퍼즐 조각에 대해
            if not used_puzzles[i]:
                puzzle = puzzle_blocks[i]
                
                # 빈칸과 퍼즐의 크기가 같으면
                if len(empty) == len(puzzle):
                    # 퍼즐을 4번 회전시키며 빈칸과 비교
                    for _ in range(4):
                        if empty == puzzle:
                            # 모양이 일치하면 칸의 개수를 더하고
                            answer += len(empty)
                            # 해당 퍼즐은 사용된 것으로 표시
                            used_puzzles[i] = True
                            # 다음 빈칸 덩어리로 넘어감
                            break
                        
                        # 퍼즐을 90도 회전
                        puzzle = rotate(puzzle)
                    
                    if used_puzzles[i]:
                        break
                        
    return answer