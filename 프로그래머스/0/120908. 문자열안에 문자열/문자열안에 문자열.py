def solution(str1, str2):
    answer = 0

    if str1.find(str2) > -1:
        answer = 1
    else:
        answer = 2

    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))    # 1
print(solution("ppprrrogrammers", "pppp"))          # 2
print(solution("AbcAbcA", "AAA"))                   # 2