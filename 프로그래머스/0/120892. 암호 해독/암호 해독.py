def solution(cipher, code):
    answer = ''

    # code의 배수 위치에 있는 문자를 answer에 추가
    for i in range(code, len(cipher)+1, code):
        answer += cipher[i-1]

    return answer

print(solution("dfjardstddetckdaccccdegk", 4))      # attack
print(solution("pfqallllabwaoclk", 2))              # fallback