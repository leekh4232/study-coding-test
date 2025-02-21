def solution(slice, n):
    answer = 0
    
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
    
    return answer

print(solution(7, 10))      # 2
print(solution(4, 12))      # 3