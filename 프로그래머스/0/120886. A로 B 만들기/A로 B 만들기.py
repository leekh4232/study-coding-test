def solution(before, after):
    # 기본적으로 만들 수 있다고 가정하고 1로 설정
    answer = 1

    # before의 각 문자를 after에서 찾음
    for b in before:
        # after에서 현재 문자의 위치 찾기
        f = after.find(b)

        # 문자가 없다면 만들 수 없으므로 0 반환
        if f == -1:
            answer = 0
            break

        # 찾은 문자를 제거하여 중복 처리 방지
        after = after[:f] + after[f+1:]

    # 최종적으로 만들 수 있는 경우 1, 그렇지 않으면 0 반환
    return answer

# ✅ 예제 테스트 실행
print(solution("olleh", "hello"))
# 결과: 1 (문자 구성과 개수가 같아 재배열 가능)

print(solution("allpe", "apple"))
# 결과: 1 (문자 구성과 개수가 같아 재배열 가능)