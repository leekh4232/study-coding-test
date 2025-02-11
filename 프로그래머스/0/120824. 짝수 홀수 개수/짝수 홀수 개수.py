def solution(num_list):
    answer = [0, 0]

    for n in num_list:
        # 어떤 수 n을 2로 나누면 짝수인 경우는 0, 홀수인 경우는 1이 된다.
        # answer에서 0번째 인덱스는 짝수의 개수, 1번째 인덱스는 홀수의 개수를 나타낸다.
        answer[n % 2] += 1

    return answer

print(solution([1, 2, 3, 4, 5]))    # [2, 3]
print(solution([1, 3, 5, 7]))       # [0, 4]