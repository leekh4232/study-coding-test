def solution(quiz):
    answer = []
    
    for q in quiz:
        expr = q.split(' ')
        
        num1 = int(expr[0])
        num2 = int(expr[2])
        num3 = int(expr[4])
        
        if expr[1] == '+':
            result = num1 + num2 == num3
        else:
            result = num1 - num2 == num3
            
        if result:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer