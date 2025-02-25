def solution(num, k):
    answer = str(num).find(str(k))  # 문자열로 변환한 num에서 k를 찾아 인덱스를 저장

    if answer > -1:  # k를 찾은 경우
        answer += 1  # 인덱스는 0부터 시작하므로 1을 더한다.

    return answer  # 최종 결과 반환

# 테스트 예제 실행
print(solution(29183, 1))  # 3
print(solution(232443, 4))  # 4
print(solution(123456, 7))  # -1