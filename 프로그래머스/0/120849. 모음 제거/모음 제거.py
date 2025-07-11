def solution(my_string):
    # 모음 제거 후 남은 문자를 저장할 문자열 변수 초기화
    answer = ''

    # 문자열을 한 글자씩 순회
    for m in my_string:
        # 현재 문자가 모음이 아닌 경우만 추가
        if m not in ['a', 'e', 'i', 'o', 'u']:
            answer += m  # 문자열에 추가

    # 최종적으로 모음이 제거된 문자열 반환
    return answer

# ✅ 예제 테스트 실행
print(solution("bus"))
# 결과: "bs" (모음 'u' 제거)

print(solution("nice to meet you"))
# 결과: "nc t mt y" (모음 'i', 'e', 'o', 'e', 'e', 'o', 'u' 제거)