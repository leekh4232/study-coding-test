def solution(n):
    prev_fact = 0
    prev_i = 0

    for i in range(n+1):
        fact = 1
        for j in range(2, i+1):
            fact *= j

        if fact <= n:
            prev_fact = fact
            prev_i = i
        else:
            break

    return prev_i

if __name__ == '__main__':
    print(solution(3628800))
    print(solution(7))