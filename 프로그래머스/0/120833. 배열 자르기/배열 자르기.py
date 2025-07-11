def solution(numbers, num1, num2):
    return numbers[num1:num2+1]  # 리스트 슬라이싱을 이용하여 부분 리스트 추출

# 테스트 예제 실행
print(solution([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
print(solution([1, 3, 5], 1, 2))        # [3, 5]
