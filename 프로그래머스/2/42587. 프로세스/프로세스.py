from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    # 우선순위 큐 생성 (높은 우선순위가 먼저 나오도록 음수 변환)
    priority_queue = PriorityQueue()
    for priority in priorities:
        priority_queue.put(-priority)  # 음수로 저장하여 최대 힙처럼 사용

    queue = deque(enumerate(priorities))  # (인덱스, 우선순위) 형태로 저장
    executed_count = 0  # 실행된 프로세스 개수

    while queue:
        current_idx, current_priority = queue.popleft()  # 맨 앞의 프로세스 꺼냄

        # 현재 프로세스가 가장 높은 우선순위인지 확인
        if current_priority < -priority_queue.queue[0]:  # 최고 우선순위가 아니라면
            queue.append((current_idx, current_priority))  # 큐의 뒤로 이동
        else:
            priority_queue.get()  # 실행된 프로세스를 우선순위 큐에서 제거
            executed_count += 1  # 실행된 프로세스 개수 증가
            if current_idx == location:  # 실행된 프로세스가 찾는 프로세스라면 실행 순서 반환
                return executed_count

# 테스트 예제 실행
print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5