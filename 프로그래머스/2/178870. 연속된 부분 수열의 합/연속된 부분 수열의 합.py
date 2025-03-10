def solution(sequence, k):
    # 투 포인터 초기화
    S, E = 0, 0  # 두 개의 포인터를 0으로 초기화
    P = sequence[0]  # 현재 부분합을 첫 번째 원소로 초기화
    min_length = float('inf')  # 최소 길이를 무한대로 설정
    answer = []  # 결과 저장 리스트

    while E < len(sequence):  # 오른쪽 포인터가 수열 범위를 넘지 않도록 설정

        if P < k:  # 부분합이 k보다 작다면
            E += 1  # 오른쪽 포인터 이동
            if E < len(sequence):  # 범위를 벗어나지 않도록 확인
                P += sequence[E]  # 새로운 값 추가

        elif P > k:  # 부분합이 k보다 크다면
            P -= sequence[S]  # 왼쪽 포인터 이동을 위해 값 제거
            S += 1  # 왼쪽 포인터 증가

        else:  # 부분합이 k와 같을 경우
            current_length = E - S  # 현재 부분 수열의 길이 계산
            if current_length < min_length:  # 최소 길이 갱신 조건 확인
                min_length = current_length  # 최소 길이 갱신
                answer = [S, E]  # 현재 인덱스 저장
            P -= sequence[S]  # 왼쪽 포인터 이동을 위해 값 제거
            S += 1  # 왼쪽 포인터 증가

    return answer  # 찾은 부분 수열의 시작 인덱스와 끝 인덱스 반환

if __name__ == "__main__":
    # 테스트 케이스 출력
    print(solution([1, 2, 3, 4, 5], 7))  # [2, 3]
    print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # [6, 6]
    print(solution([2, 2, 2, 2, 2], 6))  # [0, 2]
