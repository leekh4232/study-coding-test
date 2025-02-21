def solution(numbers, direction):
    answer = []  # 회전된 리스트를 저장할 변수

    if direction == "right":  # 오른쪽으로 회전하는 경우
        answer = numbers[-1:] + numbers[:-1]  # 마지막 원소를 앞으로 이동
    else:  # "left"인 경우 (왼쪽으로 회전)
        answer = numbers[1:] + numbers[:1]  # 첫 번째 원소를 뒤로 이동

    return answer  # 회전된 리스트 반환

# 테스트 예제 실행
print(solution([1, 2, 3], "right"))  # [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))  # [455, 6, 4, -1, 45, 6, 4]
