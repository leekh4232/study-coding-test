def solution(quiz):
    # 결과를 저장할 리스트 초기화
    answer = []

    # 각 수식을 확인
    for q in quiz:
        # 공백을 기준으로 수식을 분할
        expr = q.split(' ')

        # X, Y, Z를 정수로 변환
        num1 = int(expr[0])  # 첫 번째 숫자 (X)
        num2 = int(expr[2])  # 두 번째 숫자 (Y)
        num3 = int(expr[4])  # 결과값 (Z)

        # 연산자 확인 후 계산 수행
        if expr[1] == '+':
            result = num1 + num2 == num3
        else:
            result = num1 - num2 == num3

        # 결과가 맞으면 "O", 틀리면 "X"를 리스트에 추가
        answer.append("O" if result else "X")

    # 최종적으로 "O" 또는 "X"의 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
# 결과: ["X", "O"] (첫 번째 식은 틀림, 두 번째 식은 맞음)

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
# 결과: ["O", "O", "X", "O"] (세 번째 식만 틀림)