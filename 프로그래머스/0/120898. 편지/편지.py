def solution(message):
    answer = len(message) * 2   # 각 문자당 2cm 공간 차지
    return answer               # 계산된 가로 길이 반환

# 테스트 예제 실행
print(solution("happy birthday!"))  # 30
print(solution("I love you~"))      # 22