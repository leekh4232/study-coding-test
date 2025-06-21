def solution(array, n):
    answer = 0  # n이 등장하는 횟수를 저장할 변수

    for a in array:  # 리스트의 각 원소를 순회
        if a == n:  # 현재 원소가 n과 같다면
            answer += 1  # 등장 횟수 증가

    return answer  # 최종적으로 등장한 횟수 반환

# 테스트 예제 실행
print(solution([1, 1, 2, 3, 4, 5], 1))  # 2
print(solution([0, 2, 3, 4], 1))        # 0