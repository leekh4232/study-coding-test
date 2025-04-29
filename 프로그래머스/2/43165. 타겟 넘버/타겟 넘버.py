# 주어진 숫자들을 이용해 타겟 넘버를 만드는 경우의 수를 찾는 함수
def solution(numbers, target):
    # 스택을 이용하여 DFS 탐색을 진행
    # 각 요소는 (현재까지의 합, 현재 인덱스)를 저장
    stack = [(0, 0)]

    # 타겟 넘버를 만들 수 있는 경우의 수를 세기 위한 변수
    count = 0

    # 스택이 빌 때까지 계속 반복
    while stack:
        # 스택에서 하나 꺼내 현재 합과 현재 인덱스를 얻음
        current, idx = stack.pop()

        # 모든 숫자를 다 사용한 경우
        if idx == len(numbers):
            # 현재까지의 합이 타겟과 같다면 경우의 수를 추가
            if current == target:
                count += 1
        else:
            # 다음 숫자를 더하는 경우를 스택에 추가
            stack.append((current + numbers[idx], idx + 1))
            # 다음 숫자를 빼는 경우를 스택에 추가
            stack.append((current - numbers[idx], idx + 1))

    # 가능한 경우의 수를 반환
    return count

# 메인 코드: 테스트 케이스 실행
if __name__ == "__main__":
    # [1, 1, 1, 1, 1]로 3을 만드는 경우의 수 출력 (결과: 5)
    print(solution([1, 1, 1, 1, 1], 3))
    # [4, 1, 2, 1]로 4를 만드는 경우의 수 출력 (결과: 2)
    print(solution([4, 1, 2, 1], 4))