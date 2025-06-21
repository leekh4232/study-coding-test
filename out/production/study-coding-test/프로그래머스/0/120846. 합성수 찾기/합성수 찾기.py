def solution(n):
    answer = 0  # 합성수의 개수를 저장할 변수 초기화

    for i in range(1, n + 1):  # 1부터 n까지 반복
        count = 0  # i의 약수 개수를 세는 변수 초기화

        for j in range(1, i + 1):  # 1부터 i까지 반복하면서 약수 개수 확인
            if i % j == 0:  # i가 j로 나누어 떨어지면 약수
                count += 1  # 약수 개수 증가
                if count >= 3:  # 약수의 개수가 3개 이상이면 합성수
                    answer += 1  # 합성수 개수 증가
                    break  # 더 이상 검사할 필요 없으므로 반복 종료

    return answer  # 계산된 합성수 개수 반환

# 테스트 예제 실행
print(solution(10))  # 5
print(solution(15))  # 8
