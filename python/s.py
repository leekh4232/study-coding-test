def backtrack(path, visited, N):
    # 종료 조건: N개의 숫자를 모두 고른 경우
    if len(path) == N:
        print("결과:", path, "| visited:", bin(visited))
        return

    for i in range(1, N + 1):
        if not (visited & (1 << i)):  # i번째 숫자를 아직 사용하지 않았다면
            print(f"선택 전: i={i}, path={path}, visited={bin(visited)}")

            path.append(i)            # 경로에 추가
            visited |= (1 << i)       # i번째 숫자 사용 표시

            print(f"선택 후: i={i}, path={path}, visited={bin(visited)}")

            backtrack(path, visited, N)  # 재귀 호출

            print(f"백트래킹 전: i={i}, path={path}, visited={bin(visited)}")

            visited &= ~(1 << i)      # i번째 숫자 사용 취소 (백트래킹)
            path.pop()                # 경로에서 제거 (백트래킹)

            print(f"백트래킹 후: i={i}, path={path}, visited={bin(visited)}")

# N = 3이면 1부터 3까지의 모든 순열 출력
N = 3
backtrack([], 0, N)
