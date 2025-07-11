def solution(my_string):
    answer = 0  # 숫자의 합을 저장할 변수

    for m in my_string:  # 문자열의 각 문자를 순회
        if m.isnumeric():  # 숫자인 경우에만
            answer += int(m)  # 정수로 변환하여 더한다.

    return answer  # 최종 결과 반환

# 테스트 예제 실행
print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123"))   # 16