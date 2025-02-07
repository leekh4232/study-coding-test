def solution(hp):
    a = hp // 5
    a1 = hp % 5
    b = a1 // 3
    c = a1 % 3
    
    return a + b + c

print(solution(23))     # 결과값 : 5
print(solution(24))     # 결과값 : 6
print(solution(999))    # 결과값 : 201