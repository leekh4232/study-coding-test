from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0  # 경과 시간
    bridge = deque([0] * bridge_length)  # 다리 위의 상태 (초기에는 비어있음)
    truck_weights = deque(truck_weights)  # 대기 중인 트럭들
    current_weight = 0  # 현재 다리 위의 총 무게

    while truck_weights or current_weight > 0:
        time += 1  # 시간 증가

        # 다리에서 나갈 트럭 제거
        exiting_truck = bridge.popleft()
        current_weight -= exiting_truck  # 다리에서 제거된 트럭의 무게 감소

        # 새로운 트럭을 다리에 올릴 수 있는지 확인
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()  # 대기 중인 트럭 이동
                bridge.append(new_truck)  # 다리에 새로운 트럭 추가
                current_weight += new_truck  # 다리 무게 증가
            else:
                bridge.append(0)  # 다리에 빈 공간 추가 (트럭 이동을 대기)

    return time  # 모든 트럭이 다리를 지나간 총 시간 반환

# 테스트 예제 실행
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))  # 110