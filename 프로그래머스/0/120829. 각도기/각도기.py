def solution(angle):
    #if angle > 0 and angle < 90:
    if 0 < angle < 90:      # 예각
        return 1
    elif angle == 90:       # 직각
        return 2
    #elif angle > 90 and angle < 180:
    elif 90 < angle < 180:  # 둔각
        return 3
    elif angle == 180:      # 평각
        return 4

# ✅ 예제 테스트 실행
print(solution(70))   # 결과: 1
print(solution(91))   # 결과: 3
print(solution(180))  # 결과: 4