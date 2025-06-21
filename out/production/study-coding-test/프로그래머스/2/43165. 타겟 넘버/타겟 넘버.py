##############################################################
# Stack을 사용하는 DFS방식의 구현
##############################################################
# # 주어진 숫자들을 이용해 타겟 넘버를 만드는 경우의 수를 찾는 함수
# def solution(numbers, target):
#     # 스택을 이용하여 DFS 탐색을 진행
#     # 각 요소는 (현재까지의 합, 현재 인덱스)를 저장
#     stack = [(0, 0)]

#     # 타겟 넘버를 만들 수 있는 경우의 수를 세기 위한 변수
#     count = 0

#     # 스택이 빌 때까지 계속 반복
#     while stack:
#         # 스택에서 하나 꺼내 현재 합과 현재 인덱스를 얻음
#         current, idx = stack.pop()

#         # 모든 숫자를 다 사용한 경우
#         if idx == len(numbers):
#             # 현재까지의 합이 타겟과 같다면 경우의 수를 추가
#             if current == target:
#                 count += 1
#         else:
#             # 다음 숫자를 더하는 경우를 스택에 추가
#             stack.append((current + numbers[idx], idx + 1))
#             # 다음 숫자를 빼는 경우를 스택에 추가
#             stack.append((current - numbers[idx], idx + 1))

#     # 가능한 경우의 수를 반환
#     return count

##############################################################
# 백트래킹 방식의 구현
##############################################################
# 백트래킹을 통해 모든 경우의 수를 탐색하는 함수 정의
def backtrack(numbers, target, idx, currentSum):
    # 모든 숫자를 사용한 경우 (재귀 종료 조건)
    if idx == len(numbers):
        # 현재까지의 합이 타겟과 일치하면 유효한 경우이므로 1을 반환
        if currentSum == target:
            return 1
        # 일치하지 않으면 유효하지 않은 경우이므로 0을 반환
        else:
            return 0

    # 현재 숫자를 더한 경우를 재귀 호출
    left = backtrack(numbers, target, idx + 1, currentSum + numbers[idx])

    # 현재 숫자를 뺀 경우를 재귀 호출
    right = backtrack(numbers, target, idx + 1, currentSum - numbers[idx])

    # 두 경우를 더하여 현재 상태에서 가능한 전체 경우의 수를 반환
    return left + right

# 문제 해결을 위한 메인 함수 정의
def solution(numbers, target):
    # 인덱스 0부터 시작하고 현재 합은 0에서 출발
    return backtrack(numbers, target, 0, 0)

# 테스트용 코드
if __name__ == "__main__":
    # 예제 1: [1, 1, 1, 1, 1]로 3 만들기 (가능한 경우의 수: 5)
    print(solution([1, 1, 1, 1, 1], 3))

    # 예제 2: [4, 1, 2, 1]로 4 만들기 (가능한 경우의 수: 2)
    print(solution([4, 1, 2, 1], 4))
