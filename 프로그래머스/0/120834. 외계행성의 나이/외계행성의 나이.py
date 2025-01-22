def solution(age):
    answer = ''
    a = ord('a')
    my_age = list(map(int, str(age)))
    
    for m in my_age:
        answer += chr(m+a)
    
    return answer