def solution(number, k):
    # 숫자들을 저장할 스택 생성
    stack = []

    # 입력받은 number 문자열을 하나씩 순회
    for num in number:
        # 스택에 값이 있고, k가 남아 있으며, 스택의 마지막 값이 현재 값보다 작으면
        while k > 0 and stack and stack[-1] < num:
            stack.pop()  # 스택의 마지막 값을 제거하여 수를 키움
            k -= 1       # 제거할 수(k)를 1 감소

        # 현재 숫자를 스택에 추가
        stack.append(num)

    # 모든 순회가 끝났는데도 k가 남아있다면
    # 뒤에서 k개 만큼 제거
    if k != 0:
        stack = stack[:-k]

    # 스택에 남은 숫자들을 합쳐서 문자열로 반환
    return ''.join(stack)

# 테스트 케이스 실행
print(solution("1924", 2))      # 결과: "94"
print(solution("1231234", 3))   # 결과: "3234"
print(solution("4177252841", 4)) # 결과: "775841"