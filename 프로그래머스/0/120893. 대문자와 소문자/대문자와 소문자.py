def solution(my_string):
    answer = ''
    
    for m in my_string:
        if m.isupper():
            answer += m.lower()
        else:
            answer += m.upper()
    
    return answer