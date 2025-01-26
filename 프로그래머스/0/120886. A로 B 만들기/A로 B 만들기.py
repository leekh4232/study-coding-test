def solution(before, after):
    answer = 1
    
    for b in before:
        f = after.find(b)
        
        if f == -1:
            answer = 0
            break
            
        after = after[:f] + after[f+1:]
    
    return answer