# 계단 수의 개수를 구하는 함수
def solution(N):
    # dp[i][j] = i자리 수 중 마지막 자리가 j인 계단 수의 개수
    dp = [[0] * 10 for _ in range(N + 1)]

    # 1자리 수는 1~9만 계단 수로 인정됨 (0으로 시작 불가)
    for i in range(1, 10):
        dp[1][i] = 1

    # 결과를 10억으로 나눈 나머지를 요구함
    MOD = 1000000000

    # 2자리부터 N자리까지 계산
    for i in range(2, N + 1):
        for j in range(10):
            # 마지막 자릿수가 0이면 이전 자리는 무조건 1이어야 함
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            # 마지막 자릿수가 9이면 이전 자리는 무조건 8이어야 함
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            # 나머지는 j-1 또는 j+1에서 올 수 있음
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    # N자리 계단 수의 총 개수를 구함 (0으로 시작하는 수는 없음)
    return sum(dp[N]) % MOD

# 예시 출력
print(solution(1))  # 1자리 계단 수의 개수
print(solution(2))  # 2자리 계단 수의 개수