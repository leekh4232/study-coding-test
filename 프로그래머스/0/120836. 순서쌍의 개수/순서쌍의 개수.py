def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        # 모든 약수의 수는 순서쌍의 수와 같음
        if n % i == 0:
            answer += 1
                
    return answer