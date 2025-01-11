from collections import deque

def solution(s):
    # 문자를 저장할 deque 초기화
    stack = deque()

    # 문자열의 각 문자를 순회
    for char in s:
        # deque가 비어 있지 않고, deque의 최상단 문자와 현재 문자가 같으면
        if stack and stack[-1] == char:
            # deque의 최상단 문자를 제거
            stack.pop()
        else:
            # 그렇지 않으면 현재 문자를 deque에 추가
            stack.append(char)

    # deque가 비어 있으면 모든 문자를 짝지어 제거할 수 있었음을 의미하므로 1
    # deque가 비어 있지 않으면 짝지어 제거할 수 없는 문자가 남아 있음을 의미하므로 0
    return 1 if not stack else 0