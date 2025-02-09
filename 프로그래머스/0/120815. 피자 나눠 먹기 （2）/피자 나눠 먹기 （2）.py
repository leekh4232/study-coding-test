def solution(n):
    # 필요한 피자의 수 -> 최소 한 판 부터 시작
    answer = 1
    
    # 최대 몇 판이 필요한지 모르는 상황이므로 무한루프를 수행한다.
    while True:
        # 피자의 판 수에 조각수를 곱한 값이 모든 사람이 나누어 먹을 수 있다면 반복 중단
        if answer * 6 % n == 0:
            break

        # 반복을 중단하지 못하면 피자의 판 수를 1늘려서 반복을 계속한다.
        answer += 1
    
    return answer

print(solution(6))      # 1
print(solution(10))     # 5
print(solution(4))      # 2