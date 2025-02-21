def solution(n):
    answer = 2  # 기본적으로 n이 제곱수가 아니라고 가정

    # i를 제곱해서 n이 되기 위해서는 n의 절반보다 클 필요가 없음.
    for i in range(2, n//2):  # 2부터 n//2까지 반복 (1은 항상 제곱수의 기준이 될 수 있음)
        if i ** 2 == n:  # i를 제곱했을 때 n과 같다면?
            answer = 1  # n이 제곱수이므로 answer 값을 1로 변경
            break  # 정답을 찾았으므로 더 이상 반복할 필요 없음

    return answer  # 결과 반환

# 테스트 예제 실행
print(solution(144))  # 1 (12*12)
print(solution(979))  # 2 (제곱수가 아님)