def solution(n):
    # 필요한 피자의 최소 판 수 -> 최소 한 판부터 시작
    answer = 1

    # 최대 몇 판이 필요한지 모르는 상황이므로 무한 루프 수행
    while True:
        # 피자의 판 수(answer)에 6조각을 곱한 값이 n으로 나누어 떨어지면 반복 중단
        if answer * 6 % n == 0:
            break  # 최소한의 피자 판 수를 찾았으므로 루프 종료

        # 조건을 만족하지 못하면 피자의 판 수를 1 증가
        answer += 1

    return answer  # 계산된 최소 피자 판 수 반환

# 테스트 예제 실행
print(solution(6))  # 1
print(solution(10)) # 5
print(solution(4))  # 2