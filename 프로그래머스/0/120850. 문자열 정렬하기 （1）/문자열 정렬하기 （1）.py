def solution(my_string):
    # 숫자를 저장할 리스트 초기화
    answer = []

    # 문자열을 한 글자씩 순회
    for m in my_string:
        # 현재 문자가 숫자인지 확인 (isnumeric() 사용)
        if m.isnumeric():
            # 숫자인 경우 정수형(int)으로 변환하여 리스트에 추가
            answer.append(int(m))

    # 숫자 리스트를 오름차순 정렬
    answer.sort()

    # 정렬된 숫자 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution("hi12392"))
# 결과: [1, 2, 2, 3, 9] (숫자만 추출 후 정렬)

print(solution("p2o4i8gj2"))
# 결과: [2, 2, 4, 8] (숫자만 추출 후 정렬)

print(solution("abcde0"))
# 결과: [0] (숫자 '0'만 존재)