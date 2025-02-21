def solution(n):
    answer = 0  # 가장 큰 i 값을 저장할 변수 초기화

    # 1부터 n까지 반복 (문제 제한 사항에서 n의 최소값은 1임)
    for i in range(1, n+1):
        fact = 1  # 구하고자 하는 팩토리얼 값 초기화
        
        for j in range(2, i+1):  # 2부터 i까지 반복하여 누적곱을 구함 (팩토리얼 계산)
            fact *= j  # fact에 j를 곱하여 팩토리얼 값을 계산

        if fact <= n:  # 계산된 팩토리얼이 n보다 작거나 같다면?
            answer = i  # 현재 i가 조건을 만족하므로 answer를 갱신
        else:  # 만약 fact가 n을 초과하면 더 이상 검사할 필요 없음
            break  # 반복 종료

    # 가장 큰 i 값 반환
    return answer

# 테스트 예제 실행
print(solution(3628800))  # 10
print(solution(7))        # 3