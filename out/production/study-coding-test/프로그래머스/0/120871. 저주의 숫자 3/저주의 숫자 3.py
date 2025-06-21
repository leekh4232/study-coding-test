def solution(n):
    answer = 0  # 변환된 숫자를 저장할 변수

    for _ in range(n):  # n번 반복하여 3x 마을 숫자 찾기
        answer += 1  # 숫자를 하나씩 증가

        # 3의 배수이거나 숫자 3이 포함되면 다음 숫자로 이동
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1

    return answer  # n번째 3x 마을 숫자 반환

# ✅ 예제 테스트 실행
print(solution(15))  # 결과: 25
print(solution(40))  # 결과: 76