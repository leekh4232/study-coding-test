def solution(s1, s2):
    answer = 0  # 공통 원소 개수를 저장할 변수

    for i in s1:  # 첫 번째 리스트의 원소를 순회
        if i in s2:  # 두 번째 리스트에 동일한 원소가 존재하면
            answer += 1  # 공통 원소 개수 증가

    return answer  # 공통 원소 개수 반환

# 테스트 예제 실행
print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))   # 2
print(solution(["n", "omg"], ["m", "dot"]))                     # 0
