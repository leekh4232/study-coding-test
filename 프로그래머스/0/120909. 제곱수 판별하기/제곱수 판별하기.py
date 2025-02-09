def solution(n):
    answer = 2                  # 일단 제곱수가 아니라고 가정
    
    # i를 제곱해서 n이 되기 위해서는 n의 1/2보다 클 수 없다.
    for i in range(2, n//2):
        if i ** 2 == n:         # i의 제곱이 n이라면?
            answer = 1          # 제곱수가 맞다는 의미의 값으로 변경
            break
    
    return answer

print(solution(144))    # 1
print(solution(979))    # 2