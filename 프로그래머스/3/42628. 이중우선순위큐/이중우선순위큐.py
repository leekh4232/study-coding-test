# 이중 우선순위 큐 연산을 수행하는 함수
from heapq import heappush, heappop

def solution(operations):
    # 우선순위 큐로 사용할 리스트 초기화
    hq = []

    # 주어진 연산을 하나씩 처리
    for operation in operations:
        # 명령어와 숫자 분리
        alphabet, number = operation.split()
        number = int(number)

        # 삽입 연산인 경우
        if alphabet == 'I':
            heappush(hq, number)  # 최소 힙에 숫자 삽입

        # 삭제 연산인 경우
        else:  # alphabet == 'D'
            if hq:  # 큐가 비어있지 않을 때만 수행
                if number == -1:
                    # 최솟값 삭제 (Min-Heap의 루트)
                    heappop(hq)
                else:
                    # 최댓값 삭제를 위해 전체 정렬 후 pop
                    hq.sort()
                    hq.pop()  # 가장 큰 값 제거

    # 연산 종료 후 큐가 비어 있는지 확인
    hq.sort()  # 정렬하여 최대/최소 조회 가능하도록 함
    if hq:
        # 큐가 비어있지 않으면 [최댓값, 최솟값] 반환
        return [hq[-1], hq[0]]
    else:
        # 큐가 비어있으면 [0, 0] 반환
        return [0, 0]

# 테스트 케이스 실행
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]
