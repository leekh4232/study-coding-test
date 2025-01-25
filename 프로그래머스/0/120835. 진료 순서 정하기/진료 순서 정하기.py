def solution(emergency):
    sorted_em = sorted(emergency, reverse=True)
    
    answer = []
    
    for e in emergency:
        answer.append(sorted_em.index(e)+1)
        
    return answer