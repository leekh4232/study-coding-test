from collections import deque

def solution(stones, k):
    answer = float('inf')  # 결과를 저장할 변수, 초기값은 무한대
    q = deque()  # 윈도우 내 최대값을 관리할 deque

    for idx, stone in enumerate(stones):
        # 현재 징검다리의 값이 deque의 마지막 요소보다 크면, deque의 마지막 요소 제거
        while q and stones[q[-1]] < stone:
            q.pop()
        q.append(idx)  # 현재 징검다리의 인덱스를 deque에 추가

        # 윈도우의 범위를 벗어난 인덱스 제거
        if q[0] == idx - k:
            q.popleft()

        # 현재 idx까지의 최대값들 중 최소값 갱신
        if idx >= k - 1:
            answer = min(answer, stones[q[0]])

    return answer