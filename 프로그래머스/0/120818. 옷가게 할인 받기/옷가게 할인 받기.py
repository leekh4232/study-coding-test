def solution(price):
    answer = 0  # 최종 결제 금액을 저장할 변수 초기화

    if price >= 500000:  # 50만 원 이상 구매 시
        answer = int(price * 0.8)  # 20% 할인 적용
    elif price >= 300000:  # 30만 원 이상 구매 시
        answer = int(price * 0.9)  # 10% 할인 적용
    elif price >= 100000:  # 10만 원 이상 구매 시
        answer = int(price * 0.95)  # 5% 할인 적용
    else:  # 10만 원 미만인 경우
        answer = price  # 할인 없이 원래 가격 유지

    return answer  # 최종 결제 금액 반환

# 예제 입력 및 실행 결과 출력
print(solution(150000))  # 142500 (5% 할인 적용)
print(solution(580000))  # 464000 (20% 할인 적용)
