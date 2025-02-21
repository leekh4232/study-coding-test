def fecto(n):
    f = 1  # 팩토리얼 값을 저장할 변수, 초기값은 1
    
    for i in range(1, n+1):  # 1부터 n까지 반복하여 곱함
        f *= i  # 현재 숫자를 누적 곱셈
    
    return f  # 계산된 팩토리얼 값 반환

def solution(balls, share):
    n = balls  # 전체 구슬 개수
    k = share  # 선택할 구슬 개수
    return fecto(n) // (fecto(k) * fecto(n-k))  # 조합 공식 nCr = n! / (r! * (n-r)!) 적용하여 반환

# 테스트 예제 실행
print(solution(3, 2))  # 3
print(solution(5, 3))  # 10
