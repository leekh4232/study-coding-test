def solution(slice, n):
    answer = n // slice  # 기본적으로 필요한 피자 판 수

    if n % slice != 0:  # n이 slice로 나누어 떨어지지 않는 경우
        answer += 1  # 추가로 한 판을 더 주문해야 모든 사람이 먹을 수 있음

    return answer  # 최종적으로 필요한 피자 판 수 반환

# 테스트 예제 실행
print(solution(7, 10))  # 2
print(solution(4, 12))  # 3