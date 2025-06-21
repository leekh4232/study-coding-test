def solution(my_str, n):
    # 잘라진 문자열을 저장할 리스트 초기화
    answer = []

    # my_str이 남아있는 동안 반복
    while my_str:
        # 앞에서부터 n개의 문자 슬라이싱하여 리스트에 추가
        answer.append(my_str[:n])
        # n개만큼 잘라낸 후 나머지 문자열로 업데이트
        my_str = my_str[n:]

    # 최종적으로 분할된 문자열 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution("abc1Addfggg4556b", 6))
# 결과: ['abc1Ad', 'dfggg4', '556b'] (6글자씩 나눠서 저장)

print(solution("abcdef123", 3))
# 결과: ['abc', 'def', '123'] (3글자씩 나눠서 저장)