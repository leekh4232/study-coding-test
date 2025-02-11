def solution(numbers):
    answer = 0

    n = len(numbers)

    for i in range(0, n):
        for j in range(i+1, n):
            p = numbers[i] * numbers[j]

            if p > answer:
                answer = p

    return answer

print(solution([1, 2, 3, 4, 5]))        # 20
print(solution([0, 31, 24, 10, 1, 9]))  # 744