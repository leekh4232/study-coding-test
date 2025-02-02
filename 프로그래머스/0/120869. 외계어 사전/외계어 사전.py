def solution(spell, dic):
    answer = 2
    
    for d in dic:
        for s in spell:
            if s in d:
                answer = 1
            else:
                answer = 2
                break

        if answer ==1:
            break

    return answer