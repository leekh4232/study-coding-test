def solution(angle):
    answer = 0

    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    #elif angle > 90 and angle < 180:
    elif 90 < angle < 180:
        answer = 3
    #elif angle == 180:
    else:
        answer = 4

    return answer

# ✅ 예제 테스트 실행
print(solution(70))   # 결과: 1
print(solution(91))   # 결과: 3
print(solution(180))  # 결과: 4