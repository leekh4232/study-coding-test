def solution(numbers, target):
    # 스택을 이용하여 DFS 탐색을 진행함
    # 각 요소는 (현재까지의 합, 현재 인덱스)를 나타냄
    stack = [(0, 0)]
    
    # 타겟 숫자를 만들 수 있는 경우의 수를 저장할 변수
    count = 0

    # 스택이 빌 때까지 반복
    while stack:
        # 스택에서 하나 꺼냄
        current, idx = stack.pop()

        # 모든 숫자를 다 사용한 경우
        if idx == len(numbers):
            # 현재까지의 합이 타겟과 같다면 경우의 수 추가
            if current == target:
                count += 1
        else:
            # 다음 숫자를 더하는 경우
            stack.append((current + numbers[idx], idx + 1))
            # 다음 숫자를 빼는 경우
            stack.append((current - numbers[idx], idx + 1))

    # 가능한 경우의 수 반환
    return count

if __name__ == "__main__":
    # 테스트 케이스 실행
    print(solution([1, 1, 1, 1, 1], 3))  # 결과: 5
    print(solution([4, 1, 2, 1], 4))    # 결과: 2
