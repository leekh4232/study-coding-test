def solution(strlist):
    # 각 문자열의 길이를 저장할 리스트 초기화
    answer = []

    # 문자열 리스트를 순회하면서 각 문자열의 길이를 구함
    for s in strlist:
        # 현재 문자열의 길이를 리스트에 추가
        answer.append(len(s))

    # 최종적으로 길이 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(["We", "are", "the", "world!"]))
# 결과: [2, 3, 3, 6] (각 단어의 길이를 리스트로 반환)

print(solution(["I", "Love", "Programmers."]))
# 결과: [1, 4, 12] (각 단어의 길이를 리스트로 반환)