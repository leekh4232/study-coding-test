from collections import deque

def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과 배열 초기화
    stack = deque()  # 가격이 떨어질 가능성이 있는 인덱스를 저장할 스택

    for i, v in enumerate(prices):
        # 스택이 비어있지 않고, 현재 가격이 스택 최상단 가격보다 낮다면
        while stack and prices[stack[-1]] > v:
            j = stack.pop()  # 스택에서 인덱스 꺼내기
            answer[j] = i - j  # 가격이 유지된 기간 계산

        stack.append(i)  # 현재 인덱스 추가

    # 스택에 남아있는 인덱스들은 끝까지 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))  # 결과: [4, 3, 1, 1, 0]