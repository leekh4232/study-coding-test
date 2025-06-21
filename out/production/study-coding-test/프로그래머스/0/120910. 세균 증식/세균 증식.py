def solution(n, t):
    return n * (2 ** t)  # 세균 개수 계산

# ✅ 예제 테스트 실행
print(solution(2, 10))  # 결과: 2048
print(solution(7, 15))  # 결과: 229376