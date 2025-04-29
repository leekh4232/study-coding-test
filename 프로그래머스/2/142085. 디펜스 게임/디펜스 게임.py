# 병사의 수 n, 무적권 사용 가능 횟수 k, 각 라운드 적의 수가 담긴 배열 enemy를 받아 최대 막을 수 있는 라운드 수를 반환
def solution(n, k, enemy):
    # 이분 탐색을 위한 시작점과 끝점 초기화
    low, high = 0, len(enemy)
    
    # 정답이 될 수 있는 최대 라운드 수 저장 변수
    answer = 0

    # 이분 탐색 시작: low가 high 이하일 동안 반복
    while low <= high:
        # 중간값 계산: 현재 확인할 라운드 수
        mid = (low + high) // 2

        # 0번째 라운드부터 mid-1번째 라운드까지의 적 수 리스트 선택
        selected = enemy[:mid]

        # 무적권은 가장 많은 적 수를 가진 라운드에 써야 효율적이므로 내림차순 정렬
        selected.sort(reverse=True)

        # 무적권 k개를 사용한 뒤 남은 적들만 병사로 막아야 하므로 그 합을 구함
        total_soldiers = sum(selected[k:])

        # 병사로 막을 수 있다면 정답 갱신하고 더 많은 라운드 탐색
        if total_soldiers <= n:
            answer = mid
            low = mid + 1
        # 병사로 막을 수 없다면 더 적은 라운드만 가능한 것이므로 범위를 줄임
        else:
            high = mid - 1

    # 최대 방어 가능한 라운드 수 반환
    return answer

# 예제 테스트
print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))  # -> 5
print(solution(2, 4, [3, 3, 3, 3]))          # -> 4
