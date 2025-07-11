def solution(n):
    dp = [0] + [float('inf')] * n
    for i in range(1, n+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]

if __name__ == "__main__":
    n = int(input().strip())
    print(solution(n))
# print(solution(25))     # 1
# print(solution(26))     # 2
# print(solution(11339))  # 3
# print(solution(34567))  # 4
