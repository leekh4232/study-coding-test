def solution(num_list):
    answer = [0, 0]  # 짝수 개수와 홀수 개수를 저장할 리스트

    for n in num_list:  # 리스트의 각 원소를 순회
        answer[n % 2] += 1  # 짝수면 answer[0] 증가, 홀수면 answer[1] 증가

    return answer  # [짝수 개수, 홀수 개수] 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5]))    # [2, 3]
print(solution([1, 3, 5, 7]))       # [0, 4]