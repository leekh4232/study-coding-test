def solution(dot):
    answer = 0
    
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    
    return answer

print(solution([2, 4]))     # 1
print(solution([-7, 9]))    # 1