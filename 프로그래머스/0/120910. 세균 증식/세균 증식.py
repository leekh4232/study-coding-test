def solution(n, t):
    answer = 2 ** t * n
    return answer

print(solution(2, 10))       # 결과값 : 2048
print(solution(7, 15))       # 결과값 : 229376