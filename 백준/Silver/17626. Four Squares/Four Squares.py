import math
import sys
input = sys.stdin.readline

def solution(n):
    # 1) 1개 제곱수
    root = int(math.isqrt(n))
    if root * root == n:
        return 1

    # 2) 2개 제곱수: n = i^2 + j^2
    for i in range(1, root + 1):
        rem = n - i * i
        j = int(math.isqrt(rem))
        if j * j == rem:
            return 2

    # 3) 3개 제곱수: n = i^2 + j^2 + k^2
    # 이미 1,2개 경우가 없다는 가정
    squares = [i*i for i in range(1, root+1)]
    m = len(squares)
    for i in range(m):
        for j in range(i, m):
            rem = n - squares[i] - squares[j]
            if rem < 0:
                break
            k = int(math.isqrt(rem))
            if k*k == rem:
                return 3

    # 4) 그 외는 무조건 4개 (Lagrange 정리)
    return 4

if __name__ == "__main__":
    n = int(input().strip())
    print(solution(n))
# print(solution(25))     # 1
# print(solution(26))     # 2
# print(solution(11339))  # 3
# print(solution(34567))  # 4
