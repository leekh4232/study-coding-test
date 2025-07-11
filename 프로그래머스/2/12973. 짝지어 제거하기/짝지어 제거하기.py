from collections import deque

def solution(s):
    stack = deque()  # 스택 초기화

    for char in s:
        if stack and stack[-1] == char:  # 연속된 문자가 있으면 제거
            stack.pop()
        else:
            stack.append(char)  # 그렇지 않으면 스택에 추가

    return 1 if not stack else 0  # 스택이 비어 있으면 1, 아니면 0 반환

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution("baabaa"))  # 결과: 1
    print(solution("cdcd"))    # 결과: 0