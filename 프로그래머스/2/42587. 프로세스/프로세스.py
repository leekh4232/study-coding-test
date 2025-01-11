"""
프로그래머스 42587번 - 프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""
from queue import PriorityQueue

def solution(priorities, location):
    # 우선순위 큐 생성 (우선순위가 높은 순으로 관리)
    priority_queue = PriorityQueue()

    for idx, priority in enumerate(priorities):
        # 우선순위 큐에 음수로 저장 (높은 우선순위가 먼저 처리되도록)
        priority_queue.put((-priority, idx))

    executed = []  # 실행된 프로세스를 저장
    queue = [(priority, idx) for idx, priority in enumerate(priorities)]

    # 큐가 빌 때까지 반복 -> O(n)
    while queue:
        current_priority, current_idx = queue.pop(0)

        # 현재 프로세스가 최고 우선순위인지 확인
        # 우선순위 큐의 삽입 및 삭제 연산은 O(logN)이므로 최종적으로 이 코드의 시간 복잡도는 O(nlogN)
        if current_priority < -priority_queue.queue[0][0]:  # 최고 우선순위가 아니라면
            queue.append((current_priority, current_idx))  # 큐의 뒤로 보냄
        else:
            # 최고 우선순위 작업 실행
            priority_queue.get()  # 실행된 우선순위를 큐에서 제거
            executed.append(current_idx)  # 실행된 프로세스 저장

            # 실행한 프로세스가 원하는 위치의 프로세스라면 반환
            if current_idx == location:
                return len(executed)  # 실행 순서 반환

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))  # 1

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))  # 5
