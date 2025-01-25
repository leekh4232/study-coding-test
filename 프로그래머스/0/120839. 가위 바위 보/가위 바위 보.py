def solution(rsp):
    answer = ''
    
    mydic = {'0':'5','2':'0','5':'2'}
    
    for r in rsp:
        answer += mydic[r]
    
    return answer