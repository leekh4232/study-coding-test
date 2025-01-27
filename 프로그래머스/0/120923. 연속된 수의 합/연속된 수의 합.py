# 등차수열 문제
def solution(num, total):
    answer = []
    
    s = total // num - ((num - 1) // 2)
    
    for i in range(num):
        answer.append(s)
        s += 1
    
    return answer