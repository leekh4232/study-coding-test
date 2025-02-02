def solution(dots):
    x = []
    y = []
    
    for d in dots:
        x.append(d[0])
        y.append(d[1])
        
    width = max(x) - min(x)
    height = max(y) - min(y)
    answer = width * height
    
    return answer