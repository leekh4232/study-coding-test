def solution(n, times):
    # 최종적으로 찾을 최소 시간 (초기값은 0)
    answer = 0

    # 가능한 최소 시간: 가장 빠른 심사관의 심사 시간
    left = min(times)

    # 가능한 최대 시간: 가장 느린 심사관이 모든 사람을 심사하는 경우
    right = max(times) * n

    # 이분탐색 수행
    while left <= right:
        # 중간 시간 계산
        mid = (left + right) // 2

        # mid 시간 동안 심사할 수 있는 총 인원 수
        checked = 0

        # 모든 심사관이 mid 시간 동안 몇 명을 처리할 수 있는지 계산
        for time in times:
            # 각 심사관은 mid // time 명을 처리할 수 있음
            checked += mid // time

            # 이미 n명 이상을 처리 가능하다면 반복문 종료
            if checked >= n:
                break

        # 처리 가능한 인원이 충분한 경우: 시간을 줄여도 됨
        if checked >= n:
            # 현재 시간을 정답 후보로 저장
            answer = mid
            # 더 짧은 시간도 가능한지 확인하기 위해 right 줄임
            right = mid - 1
        else:
            # 처리 인원이 부족한 경우: 더 많은 시간이 필요하므로 left 증가
            left = mid + 1

    # 최소 시간 반환
    return answer

# 테스트 출력
print(solution(6, [7, 10]))  # -> 28
