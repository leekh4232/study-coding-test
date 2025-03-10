def solution(elements):
    res = set()                   # 결과를 저장할 집합 (중복 제거를 위해 사용)
    n = len(elements)             # 수열의 길이

    for start in range(n):        # 시작점
        win_sum = 0               # 현재 부분 수열의 합
        for length in range(n):   # 길이 1부터 n까지
            end = (start + length) % n  # 원형 수열 처리
            win_sum += elements[end]    # 부분 수열의 합 갱신
            res.add(win_sum)            # 결과 집합에 추가

    return len(res)               # 중복을 제거한 연속 부분 수열 합의 개수를 반환

if __name__ == "__main__":
    print(solution([7, 9, 1, 1, 4]))  # 18