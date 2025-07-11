def solution(slice, n):
    answer = 0  # 최소 필요한 피자 판 수를 저장할 변수
    
    if n % slice == 0:  # n이 slice로 나누어 떨어지는 경우
        answer = n // slice  # 몫만큼 피자 판을 주문하면 됨
    else:  # n이 slice로 나누어 떨어지지 않는 경우
        answer = n // slice + 1  # 추가로 한 판을 더 주문해야 모든 사람이 먹을 수 있음
    
    return answer  # 최종적으로 필요한 피자 판 수 반환

# 테스트 예제 실행
print(solution(7, 10))  # 2
print(solution(4, 12))  # 3
