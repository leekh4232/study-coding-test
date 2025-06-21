def solution(numbers):
    # 1. 배열을 정렬 (오름차순)
    numbers.sort()

    # 2. 두 가지 경우를 비교하여 최댓값 반환
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

# ✅ 예제 테스트 실행
print(solution([1, 2, -3, 4, -5]))  # 결과: 15
print(solution([0, -31, 24, 10, 1, 9]))  # 결과: 240
print(solution([10, 20, 30, 5, 5, 20, 5]))  # 결과: 600