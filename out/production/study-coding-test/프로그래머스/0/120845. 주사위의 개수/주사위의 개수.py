def solution(box, n):
    answer = 1  # 주사위 개수를 저장할 변수

    for b in box:  # box 리스트의 각 요소(가로, 세로, 높이)에 대해 반복
        answer *= b // n  # 현재 차원에서 들어갈 수 있는 주사위 개수를 곱함

    return answer  # 최종적으로 들어갈 수 있는 주사위 개수 반환

# 테스트 예제 실행
print(solution([1, 1, 1], 1))    # 1
print(solution([10, 8, 6], 3))   # 12
