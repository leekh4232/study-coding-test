def solution(dot):
    answer = 0  # 사분면 값을 저장할 변수 초기화

    if dot[0] > 0 and dot[1] > 0:  # x > 0, y > 0 → 1사분면
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:  # x < 0, y > 0 → 2사분면
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:  # x < 0, y < 0 → 3사분면
        answer = 3
    elif dot[0] > 0 and dot[1] < 0:  # x > 0, y < 0 → 4사분면
        answer = 4

    return answer  # 판별된 사분면 반환

# 테스트 예제 실행
print(solution([2, 4]))  # 1
print(solution([-7, 9])) # 2
