def solution(cipher, code):
    answer = ''  # 결과를 저장할 문자열 초기화

    # code의 배수 위치에 있는 문자를 answer에 추가
    for i in range(code, len(cipher) + 1, code):
        answer += cipher[i - 1]  # 1-based index를 맞추기 위해 i-1 사용

    return answer  # 최종 해독된 문자열 반환

# 테스트 예제 실행
print(solution("dfjardstddetckdaccccdegk", 4))  # "attack"
print(solution("pfqallllabwaoclk", 2))          # "fallback"