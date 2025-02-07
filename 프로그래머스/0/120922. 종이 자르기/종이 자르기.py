def solution(M, N):
    answer = (M-1) + M * (N-1) 
    return answer

print(solution(2, 2))       # 결과값 : 3
print(solution(2, 5))       # 결과값 : 9
print(solution(1, 1))       # 결과값 : 0