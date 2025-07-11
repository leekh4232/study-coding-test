def solution(a, b):
    # 기본적으로 무한소수라고 가정하고 2로 설정
    answer = 2

    # 유클리드 호제법을 사용하여 a와 b의 최대공약수(GCD) 구하기
    x = a
    y = b

    while y:
        x, y = y, x % y  # GCD 계산

    # 분모를 GCD로 나누어 기약분수의 분모 구하기
    b //= x

    # 분모에서 2를 제거
    while b % 2 == 0:
        b //= 2

    # 분모에서 5를 제거
    while b % 5 == 0:
        b //= 5

    # 남은 값이 1이면 유한소수, 그렇지 않으면 무한소수
    if b == 1:
        answer = 1

    return answer  # 최종 결과 반환

# ✅ 예제 테스트 실행
print(solution(7, 20))
# 결과: 1 (7/20 = 0.35 → 유한소수)

print(solution(11, 22))
# 결과: 1 (11/22 = 0.5 → 유한소수)

print(solution(12, 21))
# 결과: 2 (12/21 = 0.571428... → 무한소수)