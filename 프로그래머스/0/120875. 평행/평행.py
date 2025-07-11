def solution(dots):
    # 가능한 세 가지 직선 조합을 직접 설정하여 기울기 비교
    for (x1, y1), (x2, y2), (x3, y3), (x4, y4) in [
        (dots[0], dots[1], dots[2], dots[3]),
        (dots[0], dots[2], dots[1], dots[3]),
        (dots[0], dots[3], dots[1], dots[2])
    ]:
        # 두 직선의 기울기가 같은지 확인
        if (y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2):
            return 1  # 평행한 직선이 있으면 즉시 1 반환

    return 0  # 평행한 직선이 없으면 0 반환

# ✅ 예제 테스트 실행
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))  # 결과: 1 (평행한 직선 존재)
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))  # 결과: 0 (평행한 직선 없음)