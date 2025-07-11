# 최소 횟수로 모든 음식의 스코빌 지수를 K 이상으로 만드는 함수
import heapq

def solution(S, K):
    # Min-Heap을 구성할 빈 리스트 초기화
    heap = []

    # 모든 스코빌 지수를 힙에 삽입
    for i in S:
        heapq.heappush(heap, i)

    # 섞은 횟수를 저장할 변수
    cnt = 0

    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
    while heap[0] < K:
        # 음식을 두 개 이상 꺼낼 수 없으면 -1 반환
        if len(heap) == 1:
            return -1

        # 가장 맵지 않은 음식 꺼냄
        first = heapq.heappop(heap)

        # 두 번째로 맵지 않은 음식 꺼냄
        second = heapq.heappop(heap)

        # 새로운 음식의 스코빌 지수 계산
        newFood = first + (second * 2)

        # 새로운 음식을 힙에 추가
        heapq.heappush(heap, newFood)

        # 섞은 횟수 증가
        cnt += 1

    # 모든 음식이 K 이상일 때 섞은 횟수 반환
    return cnt

# 테스트 케이스 실행
print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
