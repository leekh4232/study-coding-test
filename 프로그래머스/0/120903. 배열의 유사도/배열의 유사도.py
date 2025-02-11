def solution(s1, s2):
    # 동일한 원소를 카운트할 변수
    answer = 0

    # 첫 번째 리스트의 원소에 대해 반복
    for i in s1:
        # 두 번째 리스트에 동일한 원소가 있다면 카운트 1 증가
        if i in s2:
            answer += 1

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))   # 2
print(solution(["n", "omg"], ["m", "dot"]))                     # 0