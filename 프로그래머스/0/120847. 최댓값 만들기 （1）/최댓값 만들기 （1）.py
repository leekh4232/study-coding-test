def solution(numbers):
    answer = 0  # 최댓값을 저장할 변수

    numbers.sort()
    answer = numbers[-1] * numbers[-2]  # 오름차순 정렬 후 최댓값 두 개의 곱

    return answer  # 최댓값 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5]))        # 20
print(solution([0, 31, 24, 10, 1, 9]))  # 744