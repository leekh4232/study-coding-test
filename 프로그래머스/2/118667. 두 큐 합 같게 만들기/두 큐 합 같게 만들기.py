def solution(queue1, queue2):
    # 두 큐의 합을 구함
    sum1, sum2 = sum(queue1), sum(queue2)
    
    # 두 큐의 합이 같아야 하는 목표 값
    target = (sum1 + sum2) // 2
    
    # 두 큐를 하나의 리스트로 합침
    combined = queue1 + queue2
    n = len(queue1)
    
    # 투 포인터 초기화
    i, j = 0, n
    
    # 현재 합을 첫 번째 큐의 합으로 초기화
    current_sum = sum1
    
    # 최대 이동 횟수는 두 큐의 길이의 합의 두 배
    max_moves = 2 * len(combined)
    moves = 0
    
    # 최대 이동 횟수 내에서 반복
    while moves < max_moves:
        # 현재 합이 목표 값과 같으면 이동 횟수 반환
        if current_sum == target:
            return moves
        # 현재 합이 목표 값보다 작으면
        elif current_sum < target:
            # 두 번째 큐에서 값을 가져와 현재 합에 더함
            current_sum += combined[j]
            # 두 번째 큐의 다음 인덱스로 이동
            j = (j + 1) % len(combined)
        else:
            # 현재 합이 목표 값보다 크면 첫 번째 큐에서 값을 빼줌
            current_sum -= combined[i]
            # 첫 번째 큐의 다음 인덱스로 이동
            i = (i + 1) % len(combined)
        # 이동 횟수 증가
        moves += 1
    
    # 최대 이동 횟수 내에 목표 값을 만들 수 없으면 -1 반환
    return -1

if __name__ == "__main__":
    # 테스트 케이스 출력
    print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
    print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
    print(solution([1, 1], [1, 5])) # -1