"""
프로그래머스 178870번 - 연속된 부분 수열의 합

https://school.programmers.co.kr/learn/courses/30/lessons/178870
"""

def solution(sequence, k):
    # 투 포인터 초기화
    left, right = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = []

    while right < len(sequence):
        if current_sum == k:
            # 현재 구간의 길이 계산
            current_length = right - left
            # 최소 길이 갱신
            if current_length < min_length:
                min_length = current_length
                answer = [left, right]
            # 왼쪽 포인터 이동
            current_sum -= sequence[left]
            left += 1
        elif current_sum < k:
            # 오른쪽 포인터 이동
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            # 왼쪽 포인터 이동
            current_sum -= sequence[left]
            left += 1

    return answer

if __name__ == "__main__":
    # 테스트 케이스 출력
    print(solution([1, 2, 3, 4, 5], 7)) # [2, 3]
    print(solution([1, 1, 1, 2, 3, 4, 5], 5)) # [6, 6]
    print(solution([2, 2, 2, 2, 2], 6)) # [0, 2]
