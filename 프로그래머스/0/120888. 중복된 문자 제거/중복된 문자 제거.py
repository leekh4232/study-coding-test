def solution(my_string):
    answer = ''  # 중복을 제거한 결과를 저장할 문자열

    for m in my_string:  # 문자열의 각 문자를 순회
        if m not in answer:  # answer에 없는 문자만 추가
            answer += m

    return answer  # 최종 변환된 문자열 반환

# 테스트 예제 실행
print(solution("people"))           # "peol"
print(solution("We are the world")) # "We arthwold"
