# 평균 반환 시간을 최소화하는 우선순위 디스크 컨트롤러 구현
import heapq

def solution(jobs):
    # 최종 반환 시간 합계 저장
    answer = 0

    # 현재 시간
    now = 0

    # 처리된 작업 수
    i = 0

    # 마지막 작업이 끝난 시점
    start = -1

    # 작업 대기 큐 (우선순위 큐)
    heap = []

    # 전체 작업이 처리될 때까지 반복
    while i < len(jobs):
        # 현재 시간까지 요청된 작업을 힙에 추가
        for job in jobs:
            request, duration = job
            if start < request <= now:
                # 힙에 (작업 소요시간, 요청 시각) 형태로 저장
                heapq.heappush(heap, [duration, request])

        # 힙에 대기 중인 작업이 있다면 처리
        if heap:
            # 가장 소요 시간이 짧은 작업 꺼내기
            current = heapq.heappop(heap)

            # 작업 시작 시각 갱신
            start = now

            # 현재 시간 증가 (작업 수행)
            now += current[0]

            # 반환 시간 = 종료 시각 - 요청 시각
            answer += now - current[1]

            # 처리된 작업 수 증가
            i += 1

        else:
            # 대기 중인 작업이 없으면 시간 1 증가 (idle)
            now += 1

    # 평균 반환 시간의 정수 부분 반환
    return answer // len(jobs)

# 테스트 케이스 실행
print(solution([[0, 3], [1, 9], [3, 5]]))  # 8
