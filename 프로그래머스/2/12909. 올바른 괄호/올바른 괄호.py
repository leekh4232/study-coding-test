from collections import deque

def solution(s):
    stack = deque()  # 스택 초기화

    for char in s:
        if char == '(':
            stack.append(char)  # 여는 괄호는 스택에 추가
        elif char == ')':
            if not stack:  # 스택이 비어있으면 False 반환 (짝 없음)
                return False
            stack.pop()  # 닫는 괄호가 나오면 스택에서 '(' 제거

    return len(stack) == 0  # 스택이 비어 있으면 True, 아니면 False

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution("()()"))     # True
    print(solution("(())()"))   # True
    print(solution(")()("))     # False
    print(solution("(()("))     # False
    print(solution("()"))       # True
    print(solution(")("))       # False
    print(solution(")"))        # False
    print(solution("("))        # False
    print(solution("))"))       # False
    print(solution("(("))       # False