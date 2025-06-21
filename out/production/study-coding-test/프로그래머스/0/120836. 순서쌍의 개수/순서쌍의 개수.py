def solution(n):
    answer = 0  # 순서쌍 개수를 저장할 변수 초기화

    for i in range(1, n+1):  # 1부터 n까지 반복
        # 모든 약수의 수는 순서쌍의 개수와 같음
        if n % i == 0:  # i가 n의 약수라면
            answer += 1  # 순서쌍 개수 증가

    return answer  # 최종적으로 구한 순서쌍 개수 반환

# 테스트 예제 실행
print(solution(20))  # 6
print(solution(100))  # 9
