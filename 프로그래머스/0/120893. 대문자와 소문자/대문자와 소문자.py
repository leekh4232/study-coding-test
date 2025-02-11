def solution(my_string):
    # [풀이1] 문자열의 모든 글자만큼 반복하여
    # 각 글자가 대문자면 소문자로, 소문자면 대문자로 변환후 answer에 추가
    # answer = ''

    # for m in my_string:
    #     if m.isupper():
    #         answer += m.lower()
    #     else:
    #         answer += m.upper()

    # return answer

    # [풀이2] 문자열의 메서드 사용
    return my_string.swapcase()

print(solution("cccCCC"))       # CCCccc
print(solution("abCdEfghIJ"))   # ABcDeFGHij