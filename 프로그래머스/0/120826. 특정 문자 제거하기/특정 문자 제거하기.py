def solution(my_string, letter):
    # [풀이1] 문자열의 replace() 메서드 사용
    #answer = my_string.replace(letter, '')

    # [풀이2] 문자열을 순회하면서 letter와 같지 않은 문자만 answer에 추가
    answer = ''

    for m in my_string:
        if m != letter:
            answer += m

    return answer

print(solution("abcdef", "f"))      # abcde
print(solution("BCBdbe", "B"))      # Cdbe