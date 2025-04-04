def solution(n):
    # 경우의 수
    answer = 0
    
    # 연속된 숫자의 시작값
    k = 1
    
    # k개의 연속된 자연수의 합이 n보다 작거나 같은지를 확인
    # -> 가우스의 덧셈공식: 1부터 k까지의 연속된 숫자의 합을 구하는 수식
    while k * (k + 1) // 2 <= n:
        if (n - (k * (k + 1) // 2)) % k == 0:
            answer += 1
        k += 1
    
    return answer