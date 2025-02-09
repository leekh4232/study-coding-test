def solution(n):
    answer = 0

    # 1부터 n까지 반복 (문제 제한 사항에서 n의 최소값은 1임)
    for i in range(1, n+1):
        fact = 1                # 구하고자 하는 팩토리얼 값
        for j in range(2, i+1): # 2부터 i까지 누적곱을 구함 -> 팩토리얼
            fact *= j

        if fact <= n:           # 팩토리얼이 n보다 작거나 같다면?
            answer = i          # answer에 i를 저장함
        else:                   # 그렇지 않다면? -> 팩토리얼이 n을 초과한다면?
            break               # 반복중단

    # 리턴값은 n을 초과하기 직전의 팩토리얼에 대한 i값이므로 주어진 범위 안에서 가장 큰 값임.
    return answer

print(solution(3628800))
print(solution(7))