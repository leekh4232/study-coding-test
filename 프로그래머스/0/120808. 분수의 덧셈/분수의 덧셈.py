def solution(numer1, denom1, numer2, denom2):
    answer = [0, 0]
    
    numer3 = denom2 * numer1 + numer2 * denom1
    denom3 = denom1 * denom2
    
    i = numer3
    
    for i in range(numer3, 0, -1):
        if numer3 % i == 0 and denom3 % i == 0:
            break
    
    answer[0] = numer3 / i
    answer[1] = denom3 / i

    return answer