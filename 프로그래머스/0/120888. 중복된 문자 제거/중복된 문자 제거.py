def solution(my_string):
    answer = ''

    for m in my_string:     # 문자열의 각 문자를 순회
        if m not in answer: # answer에 없는 문자만 추가
            answer += m

    return answer

print(solution("people"))           # peol
print(solution("We are the world")) # We arthwold