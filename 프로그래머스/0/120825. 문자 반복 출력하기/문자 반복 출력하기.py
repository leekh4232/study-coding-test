def solution(my_string, n):
    answer = ''  # 결과를 저장할 빈 문자열 초기화

    for m in my_string:  # my_string의 각 문자를 순회
        answer += m * n  # 각 문자를 n번 반복하여 answer에 추가

    return answer  # 최종 결과 반환

# 테스트 예제 실행
print(solution("hello", 3))  # "hhheeellllllooo"