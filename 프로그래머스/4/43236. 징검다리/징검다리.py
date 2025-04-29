def solution(distance, rocks, n):
    # 바위를 거리 순으로 정렬
    rocks.sort()

    # 도착지점을 마지막 바위로 간주
    rocks.append(distance)

    # 이분탐색 범위 설정
    start, end = 0, distance

    # 가능한 최대 최소 거리
    while start <= end:
        # 중간 거리(mid)를 기준으로 판단
        mid = (start + end) // 2

        cnt_remove = 0  # 제거한 바위 개수
        current = 0     # 현재 위치 (시작점)

        # 바위 간 거리를 체크하면서 최소 거리 유지 가능한지 확인
        for rock in rocks:
            dist = rock - current  # 현재 위치부터 바위까지 거리

            if dist < mid:
                # 최소 거리보다 짧으면 바위를 제거
                cnt_remove += 1
                # 제거 수가 초과되면 중단
                if cnt_remove > n:
                    break
            else:
                # 거리가 충분하면 현재 위치 갱신
                current = rock

        if cnt_remove > n:
            # 너무 많은 바위를 제거해야 하므로 거리 줄임
            end = mid - 1
        else:
            # 조건 만족하므로 거리 키워보기
            answer = mid
            start = mid + 1

    # 가능한 가장 큰 최소 거리 반환
    return answer

# 테스트
print(solution(25, [2, 14, 11, 21, 17], 2))  # -> 4
