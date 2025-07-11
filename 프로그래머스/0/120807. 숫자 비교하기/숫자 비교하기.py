def solution(num1, num2):
    answer = 0  # 결과 값을 저장할 변수를 초기화

    if num1 == num2:  # 두 숫자가 같은 경우
        answer = 1  # 결과 값에 1을 저장
    else:  # 두 숫자가 다른 경우
        answer = -1  # 결과 값에 -1을 저장

    return answer  # 최종 결과 반환

# 예제 입력 및 실행 결과 출력
print(solution(2, 3))       # -1 (2와 3은 다르므로 -1 반환)
print(solution(11, 11))     # 1 (11과 11은 같으므로 1 반환)
print(solution(7, 99))      # -1 (7과 99는 다르므로 -1 반환)