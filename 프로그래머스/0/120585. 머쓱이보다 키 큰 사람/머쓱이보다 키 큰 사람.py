def solution(array, height):
    # 카운트를 위한 변수
    answer = 0

    # 주어진 배열의 각 원소에 대해 반복
    for a in array:
        # 주어진 조건이 충족될 때 1 증가
        if a > height:
            answer += 1

    return answer

print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))       # 0