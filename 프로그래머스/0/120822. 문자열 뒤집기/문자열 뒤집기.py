def solution(my_string):
    answer = list(my_string)
    n = len(answer)
    
    for i in range(n//2):
        p = n - i - 1
        answer[i], answer[p] = answer[p], answer[i]
        
    return "".join(answer)