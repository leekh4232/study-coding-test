def solution(num_list):
    # 풀이 [1] - 파이썬 기능 사용
    #num_list.reverse()
    #return num_list
    
    # 풀이 [2] - 반대쪽 원소의 위치 구하기
    n = len(num_list)
    for i in range(n//2):
        p = n - i - 1
        num_list[i], num_list[p] = num_list[p], num_list[i]
        
    return num_list

print(solution([1, 2, 3, 4, 5]))        # [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 2]))        # [2, 1, 1, 1, 1]