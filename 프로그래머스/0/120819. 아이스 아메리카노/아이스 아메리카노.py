def solution(money):
    return [money // 5500, money % 5500]  # 최대 잔 수, 잔돈 계산 후 반환

# 테스트 예제 실행
print(solution(5500))   # [1, 0]
print(solution(15000))  # [2, 4000]