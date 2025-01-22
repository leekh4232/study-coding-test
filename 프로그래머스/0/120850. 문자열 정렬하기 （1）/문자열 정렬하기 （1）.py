def solution(my_string):
    answer = []
    my_list = []
    
    for m in my_string:
        if m.isnumeric():
            answer.append(int(m))
            
    return sorted(answer)