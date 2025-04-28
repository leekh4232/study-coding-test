def solution(number, k):
    # 남길 숫자들을 저장할 스택 생성
    stack = []

    # 입력받은 number 문자열을 왼쪽부터 하나씩 순회
    for num in number:
        # 스택이 비어있지 않고, k가 남아 있으며, 스택 마지막 숫자가 현재 숫자보다 작으면
        while k > 0 and stack and stack[-1] < num:
            stack.pop()  # 스택 마지막 숫자를 제거하여 큰 수를 만들기
            k -= 1       # 제거할 수 있는 숫자 수를 하나 줄임

        # 현재 숫자를 스택에 추가
        stack.append(num)

    # 모든 순회를 마쳤는데도 제거할 숫자(k)가 남아 있다면
    if k != 0:
        stack = stack[:-k]  # 스택의 뒤에서 남은 k개 숫자 제거

    # 스택에 남은 숫자들을 문자열로 합쳐서 반환
    return ''.join(stack)

# 테스트 케이스 실행
print(solution("1924", 2))       # 결과: "94"
print(solution("1231234", 3))    # 결과: "3234"
print(solution("4177252841", 4)) # 결과: "775841"
