def solution(my_string, letter):
    # [풀이1] replace()를 사용하여 letter를 빈 문자열로 치환
    # return my_string.replace(letter, '')

    # [풀이2] 반복문을 이용하여 letter가 아닌 문자만 추가
    answer = ''

    for m in my_string:  # 문자열의 각 문자 순회
        if m != letter:  # letter와 다른 문자만 추가
            answer += m

    return answer  # 변환된 문자열 반환

# 테스트 예제 실행
print(solution("abcdef", "f"))      # "abcde"
print(solution("BCBdbe", "B"))      # "Cdbe"