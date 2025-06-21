def solution(dots):
    # 1. x, y 좌표를 각각 저장할 리스트 초기화
    x = []
    y = []

    # 2. dots에서 x 좌표와 y 좌표를 분리하여 리스트에 추가
    for d in dots:
        x.append(d[0])
        y.append(d[1])

    # 3. 가로 길이 (x 좌표 최댓값 - 최솟값)
    width = max(x) - min(x)

    # 4. 세로 길이 (y 좌표 최댓값 - 최솟값)
    height = max(y) - min(y)

    # 5. 넓이 계산 및 반환
    return width * height

# ✅ 예제 테스트 실행
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))  # 결과: 1
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))  # 결과: 4