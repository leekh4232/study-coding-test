def fecto(n):
    f = 1

    for i in range(1, n+1):
        f *= i

    return f

def solution(balls, share):
    n = balls
    k = share
    return fecto(n) // (fecto(k) * fecto(n-k))