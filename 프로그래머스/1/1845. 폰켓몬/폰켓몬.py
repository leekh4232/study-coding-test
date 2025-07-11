# 최대한 다양한 종류의 폰켓몬을 선택할 때의 최대 종류 수를 반환하는 함수
def solution(nums):
    # 중복을 제거한 폰켓몬 종류 수 계산
    answer = len(set(nums))

    # 만약 고유 종류 수가 선택 가능한 수(N/2)보다 많다면
    # 선택 가능한 수만큼만 종류를 선택할 수 있음
    if answer > len(nums) / 2:
        return len(nums) / 2

    # 고유 종류 수가 더 적거나 같다면, 그것이 최댓값이 됨
    return answer

# 테스트 케이스 실행
print(solution([3,1,2,3]))  # 2
print(solution([3,3,3,2,2,4]))  # 3
print(solution([3,3,3,2,2,2]))  # 2
