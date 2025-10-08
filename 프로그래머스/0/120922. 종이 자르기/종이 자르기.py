def solution(M, N):
    # 세로 방향으로 (M - 1)번 자르면 M줄 생성
    verticalCuts = M - 1

    # 각 세로 조각마다 가로 방향으로 (N - 1)번 자름 → M줄 모두 잘라야 하므로 M * (N - 1)
    horizontalCuts = M * (N - 1)

    # 총 가위질 횟수는 세로 절단 + 가로 절단
    return verticalCuts + horizontalCuts


# 테스트
print(solution(2, 2)) # 3
print(solution(2, 5)) # 9
print(solution(1, 1)) # 0