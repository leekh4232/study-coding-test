def solution(numbers):
    # 주어진 리스트의 각 원소에 대해 반복
    for i in range(len(numbers)):
        # 각 원소를 2배로 변경
        numbers[i] *= 2

    return numbers  # 변경된 리스트 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5]))            # [2, 4, 6, 8, 10]
print(solution([1, 2, 100, -99, 1, 2, 3]))  # [2, 4, 200, -198, 2, 4, 6]
