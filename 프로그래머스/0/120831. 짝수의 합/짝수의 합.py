def solution(n):
    answer = 0
    
    for i in range(1, n+1):     # 1부터 n까지 반복
        if i % 2 == 0:          # i가 짝수인 경우
            answer += i         # answer에 i를 합산
            
    return answer

print(solution(10))     # 30
print(solution(4))      # 6