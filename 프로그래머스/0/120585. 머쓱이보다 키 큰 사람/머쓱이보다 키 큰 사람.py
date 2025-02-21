def solution(array, height):
    answer = 0  # 키가 더 큰 사람 수를 저장할 변수

    for a in array:  # 주어진 배열의 각 원소에 대해 반복
        if a > height:  # 머쓱이보다 키가 큰 경우
            answer += 1  # 카운트 증가

    return answer  # 키가 더 큰 사람 수 반환

# 테스트 예제 실행
print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))       # 0
