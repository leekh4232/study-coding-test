def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)

print(solution(10, 3))       # 결과값 : 124000
print(solution(64, 6))       # 결과값 : 768000