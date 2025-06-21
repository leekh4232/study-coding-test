def solution(numbers):
    # 리스트 원소의 총합 / 리스트 원소의 개수로 평균값 계산
    answer = sum(numbers) / len(numbers)
    return answer  # 계산된 평균값 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))    # 5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))  # 94.0