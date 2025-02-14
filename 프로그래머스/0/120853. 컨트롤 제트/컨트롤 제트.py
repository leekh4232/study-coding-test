def solution(s):
    # 공백을 기준으로 문자열을 리스트로 변환
    s = s.split()

    # 숫자를 저장할 리스트 초기화
    stack = []

    # 리스트를 순회하면서 숫자 또는 "Z" 처리
    for x in s:
        if x == 'Z':
            # "Z"가 나오면 마지막으로 추가한 숫자를 제거 (이전 숫자 무효화)
            stack.pop()
        else:
            # 숫자인 경우 정수로 변환하여 리스트에 추가
            stack.append(int(x))

    # 최종적으로 남아 있는 숫자들의 합을 반환
    return sum(stack)

# ✅ 예제 테스트 실행
print(solution("1 2 Z 3"))
# 결과: 4 (1 + 2 -> 2 제거(Z) -> 3 추가)

print(solution("10 20 30 40"))
# 결과: 100 (10 + 20 + 30 + 40)

print(solution("10 Z 20 Z 1"))
# 결과: 1 (10 제거 -> 20 제거 -> 1 추가)

print(solution("10 Z 20 Z"))
# 결과: 0 (10 제거 -> 20 제거 -> 남은 값 없음)

print(solution("-1 -2 -3 Z"))
# 결과: -3 (-1 + -2 + (-3 제거) = -3)