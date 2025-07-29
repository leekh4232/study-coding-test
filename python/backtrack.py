def backtrack(path, used, N):
    # 종료 조건: path 길이가 N이 되면 하나의 순열이 완성된 것이므로 출력
    if len(path) == N:
        print("결과:", path)
        return

    # 1부터 N까지의 숫자 중에서 하나씩 선택
    for i in range(1, N+1):
        if not used[i]:
            print(f"숫자 {i} 선택 전: {path}")  # 선택 전 상태 출력

            used[i] = True        # 숫자 i를 사용했다고 표시
            print("(1) --->", used)
            path.append(i)        # 현재 경로(path)에 i 추가
            print(f"숫자 {i} 선택 후: {path}")  # 선택 후 상태 출력

            print(f"숫자 {i} 백트래킹 전: {path}")  # 백트래킹 전 상태 출력
            backtrack(path, used, N)  # 재귀 호출로 다음 숫자 선택
            path.pop()            # 마지막에 추가한 숫자 제거 (백트래킹)
            used[i] = False       # 숫자 i를 다시 사용 가능하도록 되돌림
            print("(2) --->", used)
            print(f"숫자 {i} 백트래킹 후: {path}")  # 백트래킹 후 상태 출력

# N=3이면 1부터 3까지의 숫자로 만들 수 있는 순열 출력
N = 3
backtrack([], [False] * (N+1), N)