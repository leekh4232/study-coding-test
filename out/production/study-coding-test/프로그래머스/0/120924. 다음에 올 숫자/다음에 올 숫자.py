def solution(common):
    answer = 0  # 다음에 올 숫자를 저장할 변수

    # 등차수열인지 확인 (공차가 일정한 경우)
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])  # 마지막 항 + 공차

    # 등비수열인지 확인 (공비가 일정한 경우)
    elif common[1] / common[0] == common[2] / common[1]:
        answer = common[-1] * (common[1] // common[0])  # 마지막 항 * 공비

    return answer  # 다음 항 반환

# 테스트 예제 실행
print(solution([1, 2, 3, 4]))  # 5
print(solution([2, 4, 8]))     # 16
