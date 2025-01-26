def solution(numbers):
    answer = 0
    
    size = len(numbers)
    sum = 0
    
    for n in numbers:
        sum += n
    
    answer = sum / size
    
    return answer