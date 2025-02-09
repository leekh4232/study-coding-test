def solution(n):
    answer = 0                      # 합성수의 개수

    for i in range(1, n + 1):       # n이하의 자연수 이므로 1부터 n까지 반복
        count = 0                   # i의 약수에 대한 카운트 변수

        # 1부터 i까지 반복하면서 약수의 개수를 카운트한다.
        for j in range(1, i+1):
            if i % j == 0:          # j가 i의 약수라면?
                count += 1          # 카운트 1 증가
                if count >= 3:      # 약수의 개수가 3개 이상이라면?
                    answer += 1     # 합성수의 개수 1증가
                    break           # 3개를 초과하는 약수의 수는 의미 없으므로 반복 중단

    return answer

print(solution(10))     # 5
print(solution(15))     # 8