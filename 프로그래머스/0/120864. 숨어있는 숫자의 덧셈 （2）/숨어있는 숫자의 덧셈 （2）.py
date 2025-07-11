def solution(my_string):
    # 최종 합을 저장할 변수
    answer = 0

    # 문자열 길이 저장
    n = len(my_string)
    i = 0  # 인덱스 초기화

    # 문자열을 순회하면서 숫자 찾기
    while i < n:
        tmp = ""  # 숫자를 저장할 임시 변수

        # 연속된 숫자 추출
        while i < n:
            if my_string[i].isnumeric():  # 현재 문자가 숫자인 경우
                tmp += my_string[i]
                i += 1
            else:
                break  # 숫자가 끝나면 반복 종료

        # 숫자가 존재하면 정수로 변환하여 합산
        if tmp:
            answer += int(tmp)

        # 다음 문자로 이동
        i += 1

    # 최종 합 반환
    return answer

# ✅ 예제 테스트 실행
print(solution("aAb1B2cC34oOp"))
# 결과: 37 (1 + 2 + 34)

print(solution("1a2b3c4d123Z"))
# 결과: 133 (1 + 2 + 3 + 4 + 123)