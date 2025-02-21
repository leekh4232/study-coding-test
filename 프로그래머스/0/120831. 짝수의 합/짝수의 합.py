def solution(n):
    answer = 0  # 짝수들의 합을 저장할 변수 초기화

    for i in range(1, n+1):  # 1부터 n까지 반복
        if i % 2 == 0:  # i가 짝수인 경우
            answer += i  # answer에 i를 합산하여 누적

    return answer  # 최종적으로 누적된 짝수의 합 반환

# 테스트 예제 실행
print(solution(10))  # 30
print(solution(4))   # 6