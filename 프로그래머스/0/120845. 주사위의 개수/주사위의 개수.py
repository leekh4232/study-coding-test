def solution(box, n):
    #answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    #return answer
    
    answer = 1
    
    for b in box:
        answer *= b // n
        
    return answer