def solution(polynomial):
    # [x 계수 합, 상수항 합]
    vals = [0, 0]

    # 다항식을 " + " 기준으로 나누어 리스트로 변환
    poly = polynomial.split(" + ")

    # 각 항을 분석하여 계수와 상수항을 구분
    for p in poly:
        if p[0] == 'x':  # "x" 단독 (계수 1)
            vals[0] += 1
        elif p[-1] == 'x':  # "3x" 같은 형태 (계수 존재)
            vals[0] += int(p[:-1])
        else:  # 상수항
            vals[1] += int(p)

    # 최종 결과를 저장할 변수
    answer = ""

    # x 항 추가
    if vals[0] > 1:
        answer += f"{vals[0]}x"
    elif vals[0] == 1:
        answer += "x"

    # 상수항 추가
    if vals[1] > 0:
        if answer:
            answer += f" + {vals[1]}"
        else:
            answer += f"{vals[1]}"

    return answer

# ✅ 예제 테스트 실행
print(solution("3x + 7 + x"))
# 결과: "4x + 7"

print(solution("x + x + x"))
# 결과: "3x"

print(solution("5 + 3 + 7"))
# 결과: "15" (모든 항이 상수항인 경우)

print(solution("2x + 5 + x + 3"))
# 결과: "3x + 8"