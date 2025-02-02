def solution(id_pw, db):
    answer = 'fail'
    
    for d in db:
        if id_pw[0] == d[0]:
            if id_pw[1] == d[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
    
    return answer